"""Paper-trading ledger for the SPY monthly put credit spread plan. No real orders.

Rules: sell a put ~3% below SPY, buy one $10 lower, 2 spreads, ~4 weeks out.
Buy back if the cost to close (mid + $0.02/leg) reaches 2x the credit; otherwise let it expire.

Usage:
  python3 paper.py open   DATE EXPIRY SPY SHORT_K LONG_K SHORT_MID LONG_MID [SHORT_BID LONG_ASK]
  python3 paper.py mark   DATE SPY SHORT_MID LONG_MID [SHORT_ASK LONG_BID]
  python3 paper.py settle DATE SPY_CLOSE_ON_EXPIRY
"""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, 'ledger.json')
QTY, SLIP, STOP_MULT = 2, 0.02, 2.0

def load():
    if os.path.exists(LEDGER):
        return json.load(open(LEDGER))
    return {'trades': [], 'marks': []}

def save(L):
    json.dump(L, open(LEDGER, 'w'), indent=1)
    write_readme(L)

def open_trade(L, date, exp, spy, ks, kl, smid, lmid, sbid=None, lask=None):
    if any(t['status'] == 'open' for t in L['trades']):
        sys.exit('already have an open spread')
    credit = round(float(smid) - float(lmid) - 2 * SLIP, 2)
    t = dict(opened=date, expiry=exp, spy_at_open=float(spy), short_k=float(ks), long_k=float(kl),
             qty=QTY, credit=credit, stop_debit=round(credit * STOP_MULT, 2), status='open',
             natural_credit=round(float(sbid) - float(lask), 2) if sbid else None)
    L['trades'].append(t)
    print(f'OPENED {exp} {ks}/{kl} put spread x{QTY}, credit {credit:.2f} (${credit*100*QTY:.0f}), stop if debit >= {t["stop_debit"]:.2f}')

def mark(L, date, spy, smid, lmid, sask=None, lbid=None):
    t = next((t for t in L['trades'] if t['status'] == 'open'), None)
    if not t:
        print('no open spread'); return
    debit = round(float(smid) - float(lmid) + 2 * SLIP, 2)
    pnl = round((t['credit'] - debit) * 100 * t['qty'])
    L['marks'].append(dict(date=date, spy=float(spy), debit=debit, open_pnl=pnl,
                           natural_debit=round(float(sask) - float(lbid), 2) if sask else None))
    if debit >= t['stop_debit']:
        t.update(status='stopped', closed=date, exit_debit=debit, pnl=pnl)
        print(f'STOP HIT: bought back at {debit:.2f}, P&L ${pnl}')
    else:
        print(f'MARK {date}: SPY {spy}, cost to close {debit:.2f} (stop {t["stop_debit"]:.2f}), open P&L ${pnl}')

def settle(L, date, spy):
    t = next((t for t in L['trades'] if t['status'] == 'open'), None)
    if not t:
        print('no open spread'); return
    s = float(spy)
    v = max(t['short_k'] - s, 0) - max(t['long_k'] - s, 0)
    pnl = round((t['credit'] - v) * 100 * t['qty'])
    t.update(status='expired', closed=date, exit_debit=round(v, 2), spy_at_expiry=s, pnl=pnl)
    print(f'EXPIRED: SPY {s}, value {v:.2f}, P&L ${pnl}')

def write_readme(L):
    done = [t for t in L['trades'] if t['status'] != 'open']
    total = sum(t['pnl'] for t in done)
    lines = ['# Paper trading: SPY monthly put credit spreads', '',
             'Paper only, no real orders. Rules: sell a put ~3% below SPY, buy one $10 lower, 2 spreads, ~4 weeks out; '
             'buy back if it costs 2x the credit, otherwise let it expire. Updated each weekday after the close.', '',
             f'**Closed trades: {len(done)}, total P&L ${total:+,}**', '',
             '| Opened | Expiry | Strikes | Credit (x2) | Stop at | Status | P&L |', '|---|---|---|---|---|---|---|']
    for t in L['trades']:
        last = L['marks'][-1] if t['status'] == 'open' and L['marks'] else None
        pnl = f"${t['pnl']:+,}" if 'pnl' in t else (f"${last['open_pnl']:+,} (open)" if last else 'open')
        lines.append(f"| {t['opened']} | {t['expiry']} | {t['short_k']:.0f}/{t['long_k']:.0f} | "
                     f"${t['credit']*100*t['qty']:.0f} | {t['stop_debit']:.2f} | {t['status']} | {pnl} |")
    if L['marks']:
        lines += ['', '## Daily marks (last 10)', '', '| Date | SPY | Cost to close | Open P&L |', '|---|---|---|---|']
        lines += [f"| {m['date']} | {m['spy']:.2f} | {m['debit']:.2f} | ${m['open_pnl']:+,} |" for m in L['marks'][-10:]]
    open(os.path.join(HERE, 'README.md'), 'w').write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    L = load(); cmd, args = sys.argv[1], sys.argv[2:]
    {'open': open_trade, 'mark': mark, 'settle': settle}[cmd](L, *args)
    save(L)

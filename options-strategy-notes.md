# Options strategy research notes (saved 2026-09-25)

Account: Robinhood "Agentic" account (the one Claude can trade in). Currently $0 buying power,
planning ~$5,000. Options level 2 (buy calls/puts; covered calls and cash-secured puts
to be confirmed). All work so far is planning/backtesting only; no orders placed.

"Best / conservative" below: best = take-profit fills if the option touches the target
intraday; conservative = only if it closes at/above the target (the realistic one).

## Current leading plan (parked)
1. **SPY monthly calls (Test A)**: buy 1 at-the-money SPY call ~30 days out on the first
   trading day after each monthly expiration; resting sell order at +25%; otherwise hold
   to expiration. Cost ~$800–1,350/contract.
   - Jan 2022 – Sep 2026, 56 trades: +$2,785 conservative (+$4,593 best), 46/56 wins.
   - By year (cons): 2022 +$2,023 · 2023 +$25 · 2024 +$1,684 · 2025 +$905 · 2026 −$1,848.
   - $5,000 → ~$7,800 over 4.7 yrs (~10%/yr); biggest drawdown ~$2,200.
   - Hold-to-expiry (no target) made more (+$6,245) but the balance would have fallen to $536 in 2022.
   - 200-day-average filter hurt; 3% stock stop hurt.
2. **Optional add-on: cash-secured puts (Test D)** on steady ~$20 stocks (SIRI, KHC),
   ~5% below price, ~30 days out, hold to expiry.
   - Last 12 months: SIRI +$467, KHC +$259, RIOT −$214; 31/36 wins. Needs $1.2–2.9k cash per put.
3. Next step when resumed: paper-trade A (+ optional D) with a scheduled daily run, no real orders.

Benchmark: $5,000 in SPY shares from Jan 2022 → about +78% (beat every option strategy tested).

## Tested and rejected
- Whale-flow stocks (IONQ, RIOT, JETS, BB, KHC, SIRI, MTCH), 30-day calls, 40% target, 6% stock stop:
  +10% best / −14% conservative over 6 months.
- 16-combo grid (3% vs 6% stock stop, 25% vs 40% target, liquid-4 vs all-7, 30 vs 60-day):
  60-day / 6% stop / +25% target looked best (+7% to +19%), but…
- Keeping only the winners (SIRI, MTCH, BB) with 2 contracts: +21% in-sample, **−23% on the
  prior 6 months**. Picking last period's winners did not carry forward.
- IWM / XLF at-the-money calls (Test B): −18% conservative. Deep in-the-money calls (Test C): −5%.
- 10% option-price stop-loss: stopped out 22 of 24 SPY/QQQ trades, mostly same day.

## Earnings plays (tested 2026-09-25)
8 stocks (NVDA, AAPL, MSFT, AMZN, META, GOOGL, TSLA, AMD), 55 reports Jan 2025 – Aug 2026, 1 position each.
- S1 buy call 7 days before, sell report-day close: +$7,797 (+11%), won 31/53.
- S2 buy call at report-day close, sell next open: +$8,639 (+14%), won 24/55.
- S3 straddle (call+put) at report-day close, sell next open: +$20,025 (+16%), won 28/55, worst −54%. Losing months 7 of 14.
- S4 buy call 7 days before, hold through report: +$16,939 (+23%), won only 22/53; monthly swings +180% to −84%.
  Putting the whole account in every earnings month: $5,000 → ~$505.
- S5 straddle 7 days before, sell before report: −$4,328.
- Profits came mostly from META and MSFT; TSLA, NVDA, AMD lost money in most versions.
- No strategy came near 50%/month on average; earnings only occur in ~8 of 12 months.

## Monthly straddles on cheaper stocks (tested 2026-09-25)
Buy call + put at the same near-the-money strike, ~4 weeks out, every month; SOFI, RIVN, RIOT, SNAP, NIO, F.
Sep 2025 – Aug 2026, 71 trades, avg cost ~$200 per straddle.
- Every one of 48 exit-rule combinations lost money: best was +30% target, hold otherwise: −$694 (−5%).
- Skipping earnings months: best −$115 (−1%) on 47 trades. Stop-losses and early exits made it worse.
- Only RIOT made money (+$1,014, 10 of 12); SOFI −30%, SNAP −19%.
- Why: outside earnings, these stocks rarely moved enough to beat the price paid for both options.

## Lessons
- A stop based on a 6% stock drop costs ~40–80% on a 30-day option.
- Cheap/illiquid option chains have wide spreads and bad prints; index ETFs are far more reliable.
- Always check a strategy on a period that wasn't used to design it.

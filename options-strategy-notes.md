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

## Forward paper check (2026-09-21 → 2026-10-23, no real orders)
Cycle 1 (entry 9/21, expired 10/16), done:
- SPY 766 call: bought 11.96 ($1,196); it closed at 15.94 the same day, so the +25% sell at 14.95 filled → **+$299**.
  If held to expiration instead (SPY 763.25 < 766) → −$1,196. The target made the difference.
- SIRI 26 put sold 0.40 → expired worthless → **+$40**. KHC 23 put sold 0.25 → expired worthless → **+$25**
  (KHC fell to ~21.8 in early October but recovered).
Cycle 2 (entry 10/19, expires 11/20), still open as of 10/23:
- SPY 767 call bought 14.58 ($1,458). Its high on 10/21 was 18.28, just over the 18.23 target, but it closed at 17.43 that day.
  Best case: filled, +$365. Conservative: still holding, value 10.42 → −$416.
- SIRI 25.5 put sold ~0.69–0.98, now ~0.44 (open interest 0, spread 0.03/0.85: hard to fill). KHC 22.5 put sold 0.45, now 0.18 (+$27).
Total so far: conservative ≈ $0 (+$364 closed, −$390 open); best ≈ +$780. SPY shares over the same period: −0.8%.
All three together need ~$6,000 of cash; with $5,000, run SPY plus one put.

## Three alternatives vs. the current plan (tested 2026-10-25)
SPY, 14 monthly rounds: buy/sell on the Monday after the monthly expiration (Sep 2025 – Oct 2026; the Nov round is still open,
valued at the 10/23 close). $0.02 per leg added for the bid/ask gap. Each strategy sized to roughly the same amount at risk
as one SPY call (~$1,300): 1 call, or 2 spreads / 2 iron condors.
- A (current plan): 1 at-the-money call, sell at +25%.
- T (trend switch): call if SPY is above its 50-day average, otherwise a put; sell at +25%.
- CDS (call debit spread): buy the at-the-money call, sell the call $10 higher; sell at +25%. About $560 each.
- PCS (put credit spread): sell a put 3% below SPY, buy a put $10 lower; buy back at 50% of the credit. Credit ~$100–200, risk ~$860 each.
- IC (iron condor): the put spread above plus a call spread 3% above SPY; buy back at 50%. Credit ~$200–480, risk ~$660 each.

| | A (1) | T (1) | CDS (x2) | PCS (x2) | IC (x2) |
|---|---|---|---|---|---|
| 13 finished rounds, conservative | −$348 | −$2,053 | +$520 | +$336 | +$414 |
| Same, best case (fills on intraday high) | +$1,029 | −$677 | | | |
| Including the open Nov round | −$768 | −$1,769 | +$292 | +$240 | +$466 |
| Last 7 rounds (Apr–Oct 2026, current market) | −$1,426 | −$722 | −$790 | **+$890** | +$786 |
| Losing rounds out of 14 | 4 | 4 | 4 | 2 | 3 |
| Worst single round | −$1,312 | −$1,316 | −$1,176 | −$1,686 | −$1,266 |
| Biggest drop from a high | −$2,230 | −$2,970 | −$1,582 | −$1,686 | −$3,490 |
- The trend switch was the worst: the signal flipped right before rallies (Nov 2025) and right before drops.
- The put credit spread won 12 of 14 rounds. Its one big loss (Feb 2026, SPY −6%) took back about 5 months of gains.
- The iron condor lost 3 rounds in a row (Feb–Apr 2026) when SPY made big moves both ways.
- Since June, SPY has mostly stayed between 740 and 780. That suits selling spreads and hurts buying calls.

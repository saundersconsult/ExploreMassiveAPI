# Massive.com API – Forex / Currencies

**Base URL**: https://api.massive.com  
**Rate Limit**: 5 calls/minute (plan limit)  
**Status**: Reference OK; real-time snapshots forbidden (403)

## Reference Data
- ✅ GET /v3/reference/tickers?market=fx — List forex pairs
- GET /v1/conversion/{FROM}/{TO} — Currency conversion

## Historical Data
- GET /v2/aggs/ticker/C:EURUSD/prev — Previous close
- GET /v2/aggs/ticker/C:EURUSD/range/1/day/DATE1/DATE2 — Daily aggregates
- GET /v2/aggs/grouped/locale/global/market/fx/DATE — All forex aggregates

## Tick-Level Data
- GET /v3/quotes/C:AUD-USD — Historical tick quotes

## Real-Time (Forbidden – 403)
- ❌ GET /v1/last_quote/currencies/AUD/USD — Last quote

## Snapshots (Forbidden – 403)
- ❌ GET /v2/snapshot/locale/global/markets/forex/tickers — All forex snapshot
- ❌ GET /v2/snapshot/locale/global/markets/forex/gainers — Gainers
- ❌ GET /v2/snapshot/locale/global/markets/forex/losers — Losers

## Data Notes
- Coverage: 50+ currency pairs
- Historical depth: Back to 2009
- Hours: 24/5 trading
- Update frequency: Hourly to real-time

# Massive.com API – Futures

**Base URL**: https://api.massive.com  
**Rate Limit**: 5 calls/minute (plan limit)  
**Status**: Reference and historical endpoints untested

## Reference Data
- GET /futures/vX/products — All futures products
- GET /futures/vX/products/{SYMBOL} — Product details (e.g., ES for S&P 500)
- GET /futures/vX/products/{SYMBOL}/schedules — Product trading schedules
- GET /futures/vX/contracts — All contracts
- GET /futures/vX/contracts/{CONTRACT} — Contract details
- GET /futures/vX/schedules — All schedules
- GET /futures/vX/market-status — Futures market status

## Historical Data
- GET /futures/vX/aggs/{CONTRACT} — Aggregates
- GET /futures/vX/trades/{CONTRACT} — Trade data
- GET /futures/vX/quotes/{CONTRACT} — Quote data

## Example Products
- ES (S&P 500), NQ (Nasdaq), GC (Gold), CL (Crude Oil)

## Data Notes
- Coverage: Major futures across equities, commodities, bonds, currencies
- Update frequency: Real-time

## Testing Status
- Endpoints not yet exercised in this workspace

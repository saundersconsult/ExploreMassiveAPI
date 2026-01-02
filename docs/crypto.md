# Massive.com API – Crypto

**Base URL**: https://api.massive.com  
**Rate Limit**: 5 calls/minute (plan limit)  
**Status**: Core endpoints untested; real-time expected available

## Reference Data
- GET /v3/reference/tickers?market=crypto — List crypto assets

## Historical Data
- GET /v2/aggs/ticker/X:BTCUSD/prev — Previous close
- GET /v2/aggs/ticker/X:BTCUSD/range/1/day/DATE1/DATE2 — Daily aggregates
- GET /v2/aggs/grouped/locale/global/market/crypto/DATE — All crypto aggregates

## Real-Time
- GET /v1/last/crypto/BTC/USD — Last trade

## Daily Operations
- GET /v1/open-close/crypto/BTC/USD/DATE — Daily open/close

## Data Notes
- Coverage: 100+ cryptocurrencies (varies by asset)
- Historical depth: Varies by asset
- Hours: 24/7 trading
- Update frequency: Real-time

## Testing Status
- Endpoints not yet exercised in this workspace

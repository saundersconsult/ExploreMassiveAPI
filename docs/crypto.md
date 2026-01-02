# Massive.com API – Crypto

**Base URL**: https://api.massive.com  
**Rate Limit**: 5 calls/minute (plan limit)  
**Status**: Prev close & daily open/close ✅; real-time last trade ❌ (403 plan limit); other endpoints untested

## Reference Data
- GET /v3/reference/tickers?market=crypto — List crypto assets

## Historical Data
- GET /v2/aggs/ticker/X:BTCUSD/prev — Previous close
- GET /v2/aggs/ticker/X:BTCUSD/range/1/day/DATE1/DATE2 — Daily aggregates
- GET /v2/aggs/grouped/locale/global/market/crypto/DATE — All crypto aggregates

## Real-Time
- ❌ GET /v1/last/crypto/BTC/USD — Last trade (403 on current plan)

## Daily Operations
- GET /v1/open-close/crypto/BTC/USD/DATE — Daily open/close

## Data Notes
- Coverage: 100+ cryptocurrencies (varies by asset)
- Historical depth: Varies by asset
- Hours: 24/7 trading
- Update frequency: Real-time

## Symbols & Formats
- Aggregates: use `X:BASEQUOTE` (e.g., `X:BTCUSD`, `X:ETHUSD`)
- Real-time/daily paths: use `BASE/QUOTE` segments (e.g., `BTC/USD`)

## Usage Examples
- List assets: `GET /v3/reference/tickers?market=crypto&limit=50`
- Previous close: `GET /v2/aggs/ticker/X:BTCUSD/prev`
- Daily range: `GET /v2/aggs/ticker/X:BTCUSD/range/1/day/2024-01-01/2024-12-31`
- Last trade: `GET /v1/last/crypto/BTC/USD`
- Daily open/close: `GET /v1/open-close/crypto/BTC/USD/2024-01-01`

## Testing Status
- ✅ Prev close (`/v2/aggs/ticker/X:BTCUSD/prev`) returns 200
- ✅ Daily open/close (`/v1/open-close/crypto/BTC/USD/{date}`) returns 200
- ❌ Last trade real-time (`/v1/last/crypto/BTC/USD`) returns 403 (not entitled on current plan)

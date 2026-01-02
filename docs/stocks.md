# Massive.com API – Stocks / Equities

**Base URL**: https://api.massive.com  
**Rate Limit**: 5 calls/minute (plan limit)  
**Status**: Reference + daily data OK; real-time & snapshots forbidden (403)

## Reference Data
- GET /v3/reference/tickers — List/search stock tickers
- GET /v3/reference/tickers/{TICKER} — Ticker details
- GET /v3/reference/tickers/types — Available ticker types
- GET /v3/reference/conditions — Trade conditions reference
- GET /v3/reference/exchanges — List exchanges
- GET /v3/reference/dividends?ticker={TICKER} — Dividend history
- GET /v3/reference/splits — Stock splits
- GET /vX/reference/financials — Financial data
- GET /v2/reference/news — News articles
- GET /v1/related-companies/{TICKER} — Related tickers
- GET /stocks/v1/short-interest — Short interest data
- GET /stocks/v1/short-volume — Short volume data
- GET /vX/reference/tickers/{TICKER}/events — Ticker events
- GET /vX/reference/ipos — IPO calendar

## Daily & Historical Data
- ✅ GET /v1/open-close/{TICKER}/DATE — Daily OHLC
- ✅ GET /v2/aggs/ticker/{TICKER}/prev — Previous close
- GET /v2/aggs/ticker/{TICKER}/range/1/minute/DATE1/DATE2 — Minute aggregates
- GET /v2/aggs/ticker/{TICKER}/range/1/day/DATE1/DATE2 — Daily aggregates
- GET /v2/aggs/grouped/locale/us/market/stocks/DATE — All stocks aggregates

## Tick-Level Data
- GET /v3/quotes/{TICKER} — Historical tick quotes
- GET /v3/trades/{TICKER} — Historical tick trades

## Real-Time (Forbidden – 403)
- ❌ GET /v2/last/trade/{TICKER} — Last trade
- ❌ GET /v2/last/nbbo/{TICKER} — Last quote

## Market Operations
- GET /v1/marketstatus/now — Current market status
- GET /v1/marketstatus/upcoming — Market holidays

## Snapshots (Forbidden – 403)
- ❌ GET /v2/snapshot/locale/us/markets/stocks/tickers — All tickers snapshot
- ❌ GET /v2/snapshot/locale/us/markets/stocks/gainers — Gainers
- ❌ GET /v2/snapshot/locale/us/markets/stocks/losers — Losers

## Data Notes
- Coverage: ~5,000+ tickers (US/Global)
- Historical depth: Back to 2004
- Granularity: Minute/Daily/Monthly aggregates
- Update frequency: Real-time (limited), Daily (full)

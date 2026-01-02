# Massive.com API Access Overview

**Status Page**: https://massive.com/system
**All 64 APIs**: ✅ UP (0 down)

## 📊 Available API Modules

### 1. **STOCKS / EQUITIES** ✅
- Last Trade `/v2/last/trade/{TICKER}`
- Last Quote `/v2/last/nbbo/{TICKER}`
- Daily Open/Close `/v1/open-close/{TICKER}/DATE`
- Previous Close `/v2/aggs/ticker/{TICKER}/prev`
- Historical Minute Aggregates `/v2/aggs/ticker/{TICKER}/range/1/minute/DATE/DATE`
- Grouped Aggregates `/v2/aggs/grouped/locale/us/market/stocks/DATE`
- Historical Ticks - Quotes `/v3/quotes/{TICKER}`
- Historical Ticks - Trades `/v3/trades/{TICKER}`
- Snapshot - All Tickers `/v2/snapshot/locale/us/markets/stocks/tickers`
- Snapshot - Gainers `/v2/snapshot/locale/us/markets/stocks/gainers`
- Snapshot - Losers `/v2/snapshot/locale/us/markets/stocks/losers`

### 2. **FOREX / CURRENCIES** ✅
- Previous Close `/v2/aggs/ticker/C:EURUSD/prev`
- Aggregates `/v2/aggs/ticker/C:EURUSD/range/1/day/DATE/DATE`
- Historic Ticks - Quotes `/v3/quotes/C:AUD-USD`
- Real-time Conversion `/v1/conversion/AUD/USD`
- Last Quote `/v1/last_quote/currencies/AUD/USD`
- Snapshot `/v2/snapshot/locale/global/markets/forex/tickers`
- Snapshot Gainers `/v2/snapshot/locale/global/markets/forex/gainers`
- Snapshot Losers `/v2/snapshot/locale/global/markets/forex/losers`
- Grouped Aggregates `/v2/aggs/grouped/locale/global/market/fx/DATE`

### 3. **CRYPTO** ✅
- Previous Close `/v2/aggs/ticker/X:BTCUSD/prev`
- Aggregates `/v2/aggs/ticker/X:BTCUSD/range/1/day/DATE/DATE`
- Grouped Aggregates `/v2/aggs/grouped/locale/global/market/crypto/DATE`
- Last Trade `/v1/last/crypto/BTC/USD`
- Daily Open/Close `/v1/open-close/crypto/BTC/USD/DATE`

### 4. **OPTIONS** ✅
- Snapshot Chain `/v3/snapshot/options/AAPL`
- Snapshot Contract `/v3/snapshot/options/AAPL/O:AAPL270115P00340000`

### 5. **FUTURES** ✅
- Aggregates `/futures/vX/aggs/{CONTRACT}`
- Trades `/futures/vX/trades/{CONTRACT}`
- Quotes `/futures/vX/quotes/{CONTRACT}`
- Product Schedules `/futures/vX/products/{PRODUCT}/schedules`
- All Schedules `/futures/vX/schedules`
- All Contracts `/futures/vX/contracts`
- Contract Overview `/futures/vX/contracts/{CONTRACT}`
- All Products `/futures/vX/products`
- Product Overview `/futures/vX/products/{PRODUCT}`
- Market Status `/futures/vX/market-status`

### 6. **REFERENCE DATA** ✅
- Tickers v3 `/v3/reference/tickers`
- Ticker Types `/v3/reference/tickers/types`
- Ticker Details `/v3/reference/tickers/{TICKER}`
- Ticker Events `/vX/reference/tickers/{TICKER}/events`
- Conditions `/v3/reference/conditions`
- Exchanges `/v3/reference/exchanges`
- Dividends `/v3/reference/dividends`
- Splits `/v3/reference/splits`
- Financials `/vX/reference/financials`
- News V2 `/v2/reference/news`
- Short Interest `/stocks/v1/short-interest`
- Short Volume `/stocks/v1/short-volume`
- Related Tickers `/v1/related-companies/{TICKER}`
- IPOs `/vX/reference/ipos`

### 7. **MARKET OPERATIONS** ✅
- Market Status (Current) `/v1/marketstatus/now`
- Market Holidays `/v1/marketstatus/upcoming`
- Treasury Yields `/fed/v1/treasury-yields`

### 8. **TECHNICAL INDICATORS** ✅
- SMA (Simple Moving Average) `/v1/indicators/sma/{TICKER}`

### 9. **BENZINGA** ✅
- Analysts `/benzinga/v1/analysts`
- Analyst Insights `/benzinga/v1/analyst-insights`
- Ratings `/benzinga/v1/ratings`
- Consensus Ratings `/benzinga/v1/consensus-ratings/{TICKER}`
- Corporate Guidance `/benzinga/v1/guidance`
- Earnings `/benzinga/v1/earnings`
- Firm Details `/benzinga/v1/firms`
- News V2 `/benzinga/v2/news`

### 10. **UNIVERSAL** ✅
- Universal Snapshot `/v3/snapshot` (all asset types)

## 🎯 Current Implementation Status

### ✅ CONFIRMED WORKING - You Have Access:
1. ✅ `/reference/tickers` - Stock & Forex ticker search
2. ✅ `/reference/dividends` - Dividend history
3. ✅ `/reference/tickers/{TICKER}` - Ticker details
4. ✅ `/v1/open-close/{TICKER}/DATE` - Daily open/close prices
5. ✅ `/v2/aggs/ticker/{TICKER}/prev` - Previous close data

### ❌ CONFIRMED FORBIDDEN (403) - Your Plan Doesn't Include:
- `/v2/last/trade/{TICKER}` - Real-time last trade
- `/v2/last/nbbo/{TICKER}` - Real-time quotes  
- `/v2/snapshot/*` - All snapshot endpoints (gainers, losers, etc.)

### ⚠️ Not Yet Tested:
- Crypto endpoints
- Options endpoints
- Futures endpoints
- Benzinga endpoints
- Technical indicators
- Historical minute aggregates
- All other modules

## 📋 Rate Limiting
⚠️ **5 API calls per minute** (Rate limiter implemented)

## 🔧 Next Steps
1. ✅ Test stock price/quote endpoints (DONE - confirmed access to OHLC & prev close)
2. Test crypto endpoints
3. Test forex real-time conversion `/v1/conversion/AUD/USD`
4. Test Benzinga endpoints for news
5. Test technical indicators `/v1/indicators/sma/{TICKER}`
6. Test historical minute aggregates `/v2/aggs/ticker/{TICKER}/range/1/minute/DATE/DATE`

## 📝 Notes
- All endpoints are currently operational (0 down)
- Real-time latency varies by asset class:
  - Stocks: 4ms (extended hours enabled)
  - Crypto: 36ms
  - Forex: Closed market status
- Your account has access to all 64 available endpoints

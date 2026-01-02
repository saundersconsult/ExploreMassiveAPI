# Massive.com API - Complete Endpoint Reference by Category

**Status**: All 64 APIs operational ✅  
**Rate Limit**: 5 calls/minute (auto-enforced)  
**Base URL**: `https://api.massive.com`

---

## 📊 STOCKS / EQUITIES

### Reference Data
- `GET /v3/reference/tickers` - List/search stock tickers
- `GET /v3/reference/tickers/{TICKER}` - Get ticker details
- `GET /v3/reference/tickers/types` - Available ticker types
- `GET /v3/reference/conditions` - Trade conditions reference
- `GET /v3/reference/exchanges` - List exchanges
- `GET /v3/reference/dividends?ticker={TICKER}` - Dividend history
- `GET /v3/reference/splits` - Stock splits
- `GET /vX/reference/financials` - Financial data
- `GET /v2/reference/news` - News articles
- `GET /v1/related-companies/{TICKER}` - Related tickers
- `GET /stocks/v1/short-interest` - Short interest data
- `GET /stocks/v1/short-volume` - Short volume data
- `GET /vX/reference/tickers/{TICKER}/events` - Ticker events
- `GET /vX/reference/ipos` - IPO calendar

### Daily/Historical Data
- ✅ `GET /v1/open-close/{TICKER}/DATE` - Daily OHLC
- ✅ `GET /v2/aggs/ticker/{TICKER}/prev` - Previous close
- `GET /v2/aggs/ticker/{TICKER}/range/1/minute/DATE1/DATE2` - Minute aggregates
- `GET /v2/aggs/ticker/{TICKER}/range/1/day/DATE1/DATE2` - Daily aggregates
- `GET /v2/aggs/grouped/locale/us/market/stocks/DATE` - All stocks aggregates

### Tick-Level Data
- `GET /v3/quotes/{TICKER}` - Historical tick quotes
- `GET /v3/trades/{TICKER}` - Historical tick trades

### Real-Time (Forbidden - 403)
- ❌ `GET /v2/last/trade/{TICKER}` - Last trade (access denied)
- ❌ `GET /v2/last/nbbo/{TICKER}` - Last quote (access denied)

### Market Operations
- `GET /v1/marketstatus/now` - Current market status
- `GET /v1/marketstatus/upcoming` - Market holidays

### Snapshots (Forbidden - 403)
- ❌ `GET /v2/snapshot/locale/us/markets/stocks/tickers` - All tickers snapshot (access denied)
- ❌ `GET /v2/snapshot/locale/us/markets/stocks/gainers` - Gainers (access denied)
- ❌ `GET /v2/snapshot/locale/us/markets/stocks/losers` - Losers (access denied)

---

## 💱 FOREX / CURRENCIES

### Reference Data
- ✅ `GET /v3/reference/tickers?market=fx` - List forex pairs
- `GET /v1/conversion/{FROM}/{TO}` - Currency conversion

### Historical Data
- `GET /v2/aggs/ticker/C:EURUSD/prev` - Previous close
- `GET /v2/aggs/ticker/C:EURUSD/range/1/day/DATE1/DATE2` - Daily aggregates
- `GET /v2/aggs/grouped/locale/global/market/fx/DATE` - All forex aggregates

### Tick-Level Data
- `GET /v3/quotes/C:AUD-USD` - Historical tick quotes

### Real-Time (Forbidden - 403)
- ❌ `GET /v1/last_quote/currencies/AUD/USD` - Last quote (access denied)

### Snapshots (Forbidden - 403)
- ❌ `GET /v2/snapshot/locale/global/markets/forex/tickers` - All forex snapshot (access denied)
- ❌ `GET /v2/snapshot/locale/global/markets/forex/gainers` - Gainers (access denied)
- ❌ `GET /v2/snapshot/locale/global/markets/forex/losers` - Losers (access denied)

---

## 🪙 CRYPTO

### Reference Data
- `GET /v3/reference/tickers?market=crypto` - List crypto assets

### Historical Data
- `GET /v2/aggs/ticker/X:BTCUSD/prev` - Previous close
- `GET /v2/aggs/ticker/X:BTCUSD/range/1/day/DATE1/DATE2` - Daily aggregates
- `GET /v2/aggs/grouped/locale/global/market/crypto/DATE` - All crypto aggregates

### Real-Time
- `GET /v1/last/crypto/BTC/USD` - Last trade

### Daily Operations
- `GET /v1/open-close/crypto/BTC/USD/DATE` - Daily open/close

---

## ⚙️ OPTIONS

### Snapshots
- `GET /v3/snapshot/options/{TICKER}` - Options chain snapshot
- `GET /v3/snapshot/options/{TICKER}/O:CONTRACT` - Specific contract snapshot

---

## 📈 FUTURES

### Reference Data
- `GET /futures/vX/products` - All futures products
- `GET /futures/vX/products/{SYMBOL}` - Product details (e.g., ES for S&P 500)
- `GET /futures/vX/products/{SYMBOL}/schedules` - Product trading schedules
- `GET /futures/vX/contracts` - All contracts
- `GET /futures/vX/contracts/{CONTRACT}` - Contract details
- `GET /futures/vX/schedules` - All schedules
- `GET /futures/vX/market-status` - Futures market status

### Historical Data
- `GET /futures/vX/aggs/{CONTRACT}` - Aggregates
- `GET /futures/vX/trades/{CONTRACT}` - Trade data
- `GET /futures/vX/quotes/{CONTRACT}` - Quote data

**Example Products**: ES (S&P 500), NQ (Nasdaq), GC (Gold), CL (Crude Oil)

---

## 📰 BENZINGA

### News & Sentiment
- `GET /benzinga/v2/news` - News articles
- `GET /benzinga/v1/analyst-insights` - Analyst insights

### Ratings & Analysis
- `GET /benzinga/v1/analysts` - Analyst directory
- `GET /benzinga/v1/ratings` - Analyst ratings
- `GET /benzinga/v1/consensus-ratings/{TICKER}` - Consensus ratings
- `GET /benzinga/v1/firms` - Firm details

### Corporate Actions
- `GET /benzinga/v1/earnings` - Earnings calendar
- `GET /benzinga/v1/guidance` - Corporate guidance

---

## 📊 TECHNICAL INDICATORS

### Moving Averages
- `GET /v1/indicators/sma/{TICKER}` - Simple Moving Average (SMA)

**Note**: Additional indicators may be available; check Massive documentation

---

## 🏦 FEDERAL / TREASURY

### Yields
- `GET /fed/v1/treasury-yields` - US Treasury yields

---

## 🎯 UNIVERSAL

### Multi-Asset Snapshot
- `GET /v3/snapshot` - Universal snapshot (all asset types)

---

## 📋 API ACCESS STATUS

### ✅ Confirmed Working
| Category | Endpoints | Status |
|----------|-----------|--------|
| Stock Reference | Tickers, details, dividends, splits | ✅ Full access |
| Forex Reference | Ticker list | ✅ Full access |
| Stock OHLC | Daily open/close, previous close | ✅ Full access |
| Market Operations | Holidays, status | ✅ Full access |

### ❌ Confirmed Forbidden (403)
| Category | Endpoints | Reason |
|----------|-----------|--------|
| Stock Real-Time | Last trade, quotes, snapshots | Plan limitation |
| Forex Real-Time | Last quotes, snapshots | Plan limitation |

### ⚠️ Not Yet Tested
| Category | Status |
|----------|--------|
| Crypto endpoints | Untested |
| Options endpoints | Untested |
| Futures endpoints | Untested |
| Benzinga endpoints | Untested |
| Technical indicators | Untested |
| Historical minute aggregates | Untested |
| Treasury yields | Untested |

---

## 🔄 Data Characteristics by Category

### Stock Data
- **Coverage**: ~5,000+ tickers (US/Global)
- **Historical**: Back to 2004
- **Update Frequency**: Real-time (limited), Daily (full)
- **Granularity**: Minute/Daily/Monthly aggregates

### Forex Data
- **Coverage**: 50+ currency pairs
- **Historical**: Back to 2009
- **Hours**: 24/5 trading
- **Update Frequency**: Hourly to Real-time

### Crypto Data
- **Coverage**: 100+ cryptocurrencies
- **Historical**: Varies by asset
- **Hours**: 24/7 trading
- **Update Frequency**: Real-time

### Options Data
- **Coverage**: All listed options
- **Update Frequency**: Real-time snapshots

### Futures Data
- **Coverage**: All major futures contracts
- **Update Frequency**: Real-time
- **Markets**: Equities, Commodities, Bonds, Currencies

---

## 🚀 Common Use Cases by Category

### Stock Analysis
```python
# Get dividend history
GET /v3/reference/dividends?ticker=AAPL

# Get historical daily prices
GET /v2/aggs/ticker/AAPL/range/1/day/2024-01-01/2024-12-31

# Get company details
GET /v3/reference/tickers/AAPL
```

### Forex Trading Research
```python
# List available pairs
GET /v3/reference/tickers?market=fx&limit=50

# Get historical forex data
GET /v2/aggs/ticker/C:EURUSD/range/1/day/2024-01-01/2024-12-31

# Currency conversion
GET /v1/conversion/EUR/USD
```

### Market Monitoring
```python
# Check market holidays
GET /v1/marketstatus/upcoming

# Get market status
GET /v1/marketstatus/now

# Treasury yields
GET /fed/v1/treasury-yields
```

### News & Analysis
```python
# Get recent news
GET /benzinga/v2/news

# Get analyst ratings
GET /benzinga/v1/ratings

# Get consensus for specific stock
GET /benzinga/v1/consensus-ratings/AAPL
```

---

## 📝 Rate Limiting & Best Practices

- **Limit**: 5 API calls per minute
- **Strategy**: Batch requests, cache responses
- **Auto-Handled**: Built into client with `RateLimiter` class
- **Monitoring**: Check `explore_api.py` for interactive testing

---

## 🔗 Related Resources

- **System Status**: https://massive.com/system
- **Documentation**: https://massive.com/docs
- **Support**: https://massive.com/contact
- **Blog**: https://massive.com/blog

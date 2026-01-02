# Massive.com API - Endpoint Reference (Index)

**Status**: All 64 APIs operational ✅  
**Rate Limit**: 5 calls/minute (auto-enforced)  
**Base URL**: https://api.massive.com

Use these per-category references:

- [docs/stocks.md](stocks.md)
- [docs/forex.md](forex.md)
- [docs/crypto.md](crypto.md)
- [docs/options.md](options.md)
- [docs/futures.md](futures.md)
- [docs/benzinga.md](benzinga.md)
- [docs/technical-indicators.md](technical-indicators.md)
- [docs/federal.md](federal.md)
- [docs/universal.md](universal.md)

## 📋 API Access Status

### ✅ Confirmed Working
| Category | Endpoints | Status |
|----------|-----------|--------|
| Stock Reference | Tickers, details, dividends, splits | ✅ Full access |
| Forex Reference | Ticker list | ✅ Full access |
| Stock OHLC | Daily open/close, previous close | ✅ Full access |
| Market Operations | Holidays, status | ✅ Full access |
| Crypto Daily | Prev close, open/close | ✅ Working |
| Crypto Aggregates | Range + grouped daily | ✅ Working |

### ❌ Confirmed Forbidden (403)
| Category | Endpoints | Reason |
|----------|-----------|--------|
| Stock Real-Time | Last trade, quotes, snapshots | Plan limitation |
| Forex Real-Time | Last quotes, snapshots | Plan limitation |
| Crypto Real-Time | Last trade | Plan limitation |

### ⚠️ Not Yet Tested
| Category | Status |
|----------|--------|
| Options endpoints | Untested |
| Futures endpoints | Untested |
| Benzinga endpoints | Untested |
| Technical indicators | Untested |
| Historical minute aggregates | Untested |
| Treasury yields | Untested |

---

## 🔄 Data Characteristics by Category

- Stocks: ~5,000+ tickers; back to 2004; minute/daily/monthly
- Forex: 50+ pairs; back to 2009; 24/5; hourly to real-time
- Crypto: 100+ assets; 24/7; real-time
- Options: All listed; real-time snapshots
- Futures: Major contracts across equities/commodities/bonds/currencies; real-time

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

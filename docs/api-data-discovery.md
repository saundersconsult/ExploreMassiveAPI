# Massive.com API - Complete Data Discovery

## 📊 Available Data & Endpoints

### 1. **Forex (Currency Pairs)**
- **Endpoint**: `/reference/tickers?market=fx`
- **Data**: 50+ currency pairs available
- **Examples**: EUR/USD, GBP/USD, AUD/JPY, etc.
- **Format**: `C:EURUSD` (C: prefix for cryptocurrency/forex)

### 2. **Stock Dividends**
- **Endpoint**: `/reference/dividends?ticker=AAPL`
- **Data**: Historical dividend records with amounts and ex-dividend dates
- **Examples**: AAPL has 10 dividend records, MSFT has regular quarterly dividends
- **Note**: TSLA has no dividend records

### 3. **Stock Tickers & Reference Data**
- **Endpoint**: `/reference/tickers?search=apple&limit=100`
- **Data**: 
  - Ticker symbol and name
  - Market type (stocks, fx, crypto, indices, otc)
  - Active/inactive status
  - Currency information
  - Exchange codes (XNAS, XNYS, etc.)

### 4. **Ticker Details**
- **Endpoint**: `/reference/tickers/{TICKER}`
- **Data**:
  - Company name
  - Market cap (for stocks)
  - Headquarters address
  - Active status
  - Type (CS = Common Stock, ETF, etc.)
  - Primary exchange

## 📋 Rate Limiting

⚠️ **5 calls per minute** - Rate limiter automatically built into API client

## 🔍 Available Markets

- **Stocks** (US/Global)
- **Forex** (50+ currency pairs)
- **Crypto** (if enabled)
- **Indices** (market indices)
- **OTC** (over-the-counter)

## 🚀 Sample Usage

```python
from src.api_client import MassiveAPIClient

client = MassiveAPIClient()

# Get dividends
dividends = client.get_dividends("AAPL")

# Search tickers
tickers = client._make_request("/reference/tickers", params={"search": "apple"})

# Get ticker details
details = client._make_request("/reference/tickers/AAPL")

# List forex pairs
forex = client._make_request("/reference/tickers", params={"market": "fx", "limit": 50})
```

## 📝 Notes

- All rate limiting handled automatically
- API key stored in `config/massive.env`
- Supports pagination via `next_url` field
- Data updates hourly to daily depending on plan

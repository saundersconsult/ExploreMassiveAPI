# Massive.com API Endpoints

## Overview

Massive.com (formerly Polygon) provides REST API, WebSocket, and Flat Files access to market data.

**Base URL**: `https://api.massive.com/v3`

**Authentication**: API key via query parameter (`?apiKey=YOUR_KEY`) or `Authorization: Bearer YOUR_KEY` header

**Official Python Client**: https://github.com/massive-com/client-python

## Discovered Endpoints

### Market Operations

#### Market Holidays ✅ WORKING
```
GET /v1/marketstatus/upcoming
Query Parameters:
  - apiKey: Your API key

Returns: Array of trading market holidays with status
  {
    "date": "2026-01-19",
    "exchange": "NASDAQ",
    "name": "Martin Luther King, Jr. Day",
    "status": "closed" | "early-close",
    "open": "HH:MM:SS.000Z" (if early-close),
    "close": "HH:MM:SS.000Z" (if early-close)
  }
```

**Status**: ✅ Tested and confirmed working
**Use Case**: Block trading signals on market closures; adjust for early closes
**Trading Holidays**: Thanksgiving, Christmas, Independence Day, MLK Day, Presidents Day, Memorial Day, Labor Day, Good Friday, Juneteenth, etc.

#### Dividends (✅ WORKING)
```
GET /reference/dividends
Query Parameters:
  - ticker: Stock symbol (e.g., "AAPL")
  - apiKey: Your API key

Returns:
  {
    "status": "OK",
    "results": [
      {
        "ticker": "AAPL",
        "ex_dividend_date": "2025-11-10",
        "cash_amount": 0.26,
        "dividend_type": "CD",
        "declaration_date": "2025-10-30",
        "record_date": "2025-11-10",
        "pay_date": "2025-11-13",
        "currency": "USD",
        "frequency": 4,
        "id": "E46d7ebe..."
      }
    ]
  }
```

**Use Case**: Track dividend events for trading logic
**Status**: ✅ Tested and confirmed working

### Market Data

#### Market Hours
```
GET /markets/{market}/hours
Path Parameters:
  - market: Market identifier

Query Parameters:
  - apiKey: Your API key

Returns:
  Trading hours, market status, etc.
```

**Status**: Endpoint structure known; needs exploration

## API Client Options

### Official Python Client

```bash
pip install massive-com
```

```python
from massive import RESTClient

client = RESTClient(api_key="YOUR_KEY")

# Get holidays
holidays = client.reference.get_holidays(exchange="NASDAQ")

# Get dividends
dividends = client.reference.get_dividends(ticker="AAPL")
```

### Manual REST

Use with `requests` library:

```python
import requests

api_key = "YOUR_KEY"
response = requests.get(
    "https://api.massive.com/v3/reference/holidays",
    params={"exchange": "NASDAQ", "apiKey": api_key}
)
data = response.json()
```

## Integration Status

| Endpoint | Status | Integration |
|----------|--------|-------------|
| /v1/marketstatus/upcoming | ✅ Working | api_client.py, holiday_fetcher.py (TRADING holidays) |
| /reference/dividends | ✅ Working | api_client.py, tested |
| /markets/{market}/hours | ❓ Unknown | Not tested |

## Alternative Holiday Sources

**NOT NEEDED** - Massive.com API now provides trading holidays! 

But here are alternatives if you need them:

### 1. **NASDAQ/NYSE Holiday Calendar (Free)**

Download ICS files or scrape:
- https://www.nasdaq.com/market-activity/trading-hours-and-holidays
- https://www.nyse.com/publicdocs/nyse/trading/Trading_Schedule.pdf

### 2. **Google Calendar API (Free tier)**

Query public Google Calendar for market holidays:

```python
from googleapiclient.discovery import build

service = build('calendar', 'v3', developerKey='YOUR_KEY')
events = service.events().list(
    calendarId='nasdaq.com_g27s4bd0a0l62n6mq648lnq4t4@group.calendar.google.com',
    timeMin='2026-01-01T00:00:00Z'
).execute()
```

### 3. **holidays-ics Python Package (Free)**

```bash
pip install holidays
```

```python
import holidays
import datetime

nasdaq_holidays = holidays.US(years=2026)
today = datetime.date.today()

if today in nasdaq_holidays:
    print(f"Market closed: {nasdaq_holidays[today]}")
```

### 4. **Broker Holiday Calendars**

- **MT5**: Use `mt5.copy_rates_from()` with validation for holidays
- **Interactive Brokers**: Use their API holiday feed
- **Alpaca**: Check `market_calendar` in their API

### 5. **Custom Hardcoded List (Simple)**

```python
US_MARKET_HOLIDAYS = {
    (1, 1): "New Year's Day",
    (1, 20): "MLK Jr. Day",
    (2, 17): "Presidents' Day",
    (3, 17): "Good Friday",
    # ... add more
}
```

## Recommended Approach for Your Project

**Use Massive.com Market Holidays API** (native solution):

```python
# Install
pip install -r requirements.txt

# Use in code
from holiday_fetcher import HolidayFetcher

fetcher = HolidayFetcher("NASDAQ")

# Check if market is closed
if fetcher.is_market_closed():
    logger.info("Market closed - skip trading")
    return

# Check for early closes
if fetcher.is_early_close():
    early_close = fetcher.get_early_close_time()
    logger.info(f"Market closes early at {early_close}")

# Get holiday details
holiday = fetcher.get_holiday_info()
if holiday:
    print(f"Holiday: {holiday['name']} - {holiday['status']}")
```

**Advantages**:
- ✅ Real trading market holidays only (no calendar noise)
- ✅ Includes early-close times for Thanksgiving, day after Thanksgiving
- ✅ Native Massive.com integration (same API key)
- ✅ Always current (refreshes daily)

## Testing

### Manual Testing

```bash
# Interactive explorer
python src/api_explorer.py

# Holiday fetcher test
python src/holiday_fetcher.py
```

### Unit Tests

```bash
pytest tests/ -v
```

## References

- **Massive.com Docs**: https://massive.com/docs
- **REST API Quickstart**: https://massive.com/docs/rest/quickstart
- **Python Client**: https://github.com/massive-com/client-python
- **Python Client Docs**: https://github.com/massive-com/client-python/blob/main/README.md

## API Key Management

**DO NOT commit API keys!**

Store in:
- `config/massive.env` (excluded by .gitignore)
- Environment variables
- GitHub Secrets (for CI/CD)

Example `.env`:
```
MASSIVE_API_KEY=pJn4UG5755d8QtnOxIW1ypXlMVPL6Nr4
```

## Rate Limits

Check Massive.com documentation for rate limit details. Typically include:
- Requests per minute
- Requests per month
- Concurrent connections

## Errors

Common API errors:

| Status | Meaning |
|--------|---------|
| 401 | Invalid or missing API key |
| 404 | Endpoint not found |
| 429 | Rate limited |
| 500 | Server error |

## Next Steps

1. ✅ Set up project structure
2. ✅ Create API client wrapper
3. ⏳ Test holidays endpoint with real API
4. ⏳ Integrate into Signals-Telegram-MT5
5. ⏳ Explore additional endpoints
6. ⏳ Add WebSocket support if needed

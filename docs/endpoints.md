# Massive.com API Endpoints

## Overview

Massive.com (formerly Polygon) provides REST API, WebSocket, and Flat Files access to market data.

**Base URL**: `https://api.massive.com/v3`

**Authentication**: API key via query parameter (`?apiKey=YOUR_KEY`) or `Authorization: Bearer YOUR_KEY` header

**Official Python Client**: https://github.com/massive-com/client-python

## Discovered Endpoints

### Reference Data

#### Holidays
```
GET /reference/holidays
Query Parameters:
  - exchange: Exchange code (NASDAQ, NYSE, AMEX, etc.)
  - apiKey: Your API key

Status: ❌ NOT AVAILABLE in Massive.com API (404 error)
```

**Note**: Massive.com does not expose a holidays/trading calendar endpoint. See [Alternative Holiday Sources](#alternative-holiday-sources) for workarounds.

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
| /reference/dividends | ✅ Working | api_client.py, tested |
| /reference/holidays | ❌ Not Available | Use alternative sources |
| /markets/{market}/hours | ❓ Unknown | Not tested |

## Alternative Holiday Sources

Since Massive.com doesn't provide a holidays endpoint, use these alternatives:

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

**Use `holidays` Python package** (simplest and most reliable):

```python
# Install
pip install holidays

# Use in holiday_fetcher.py
import holidays
from datetime import date

def is_market_holiday(check_date=None, exchange="NASDAQ"):
    """Check if date is a US market holiday."""
    check_date = check_date or date.today()
    us_holidays = holidays.US(years=check_date.year)
    return check_date in us_holidays
```

This integrates cleanly without requiring API keys or external dependencies (except holidays package).

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

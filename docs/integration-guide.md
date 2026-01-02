# Integration with Signals-Telegram-MT5

## Overview

This guide explains how to integrate Massive.com holiday data with the Signals-Telegram-MT5 listener to prevent trading on market closure days.

## Architecture

```
ExploreMassiveAPI (this repo)
  └─ HolidayFetcher
      └─ Polls /reference/holidays endpoint
          └─ Caches exchange holidays

Signals-Telegram-MT5
  └─ News Blackout Manager
      └─ Uses holiday calendar to block trades
```

## Integration Steps

### 1. Wire Holiday Fetcher into Listener

Update `src/main.py` in Signals-Telegram-MT5:

```python
from holiday_fetcher import HolidayFetcher

# In listener initialization
holiday_fetcher = HolidayFetcher(exchange=cfg.trading.exchange)

# Before executing trades
if holiday_fetcher.is_holiday():
    logger.info(f"Market closed today - skipping signal")
    return
```

### 2. Configure Exchange

In `config.yaml`:

```yaml
holidays:
  enabled: true
  exchange: NASDAQ  # or NYSE, AMEX, etc.
  poll_interval_hours: 24
```

### 3. Test with Preview Tool

```bash
python holiday_fetcher.py
```

Verify:
- Holidays are fetched correctly
- Today's status is accurate
- Next trading day calculation is correct

## API Key Management

Store Massive.com API key in environment:

**Windows PowerShell:**
```powershell
$env:MASSIVE_API_KEY = "pJn4UG5755d8QtnOxIW1ypXlMVPL6Nr4"
```

**Or in `.env` file** (never commit):
```
MASSIVE_API_KEY=pJn4UG5755d8QtnOxIW1ypXlMVPL6Nr4
```

## Testing

Create integration test in Signals-Telegram-MT5:

```python
from holiday_fetcher import HolidayFetcher

def test_holiday_blocks_trade():
    fetcher = HolidayFetcher("NASDAQ")
    
    # Test that a known holiday is recognized
    assert fetcher.is_holiday(date(2026, 1, 1))  # New Year's Day
```

## Monitoring

Log holiday-related trade blocks:

```python
logger.info(f"Trade blocked: Market holiday ({holiday_name})")
```

## Troubleshooting

**Issue**: Holiday data not fetching
- Check API key is valid
- Verify exchange code is correct
- Check network connectivity

**Issue**: Stale holiday data
- Increase poll frequency
- Force refresh before signal execution

**Issue**: Weekend filtering not working
- Verify date parsing (timezone considerations)
- Check that weekday() logic includes Saturday(5) and Sunday(6)


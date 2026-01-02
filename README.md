# ExploreMassiveAPI

Exploration and integration of Massive.com APIs for trading automation, with focus on market holidays to prevent trading during market closures.

## Features

- **Market Holidays Fetcher**: Pull exchange holidays to block trading signals
- **API Explorer**: Systematic exploration of Massive.com's available endpoints
- **Reference Data**: Dividends, splits, corporate actions
- **Exchange Data**: Market hours, holidays, trading calendars
- **Per-Category Docs**: Stocks, Forex, Crypto, Options, Futures, Benzinga, Technical, Treasury, Universal snapshot

## Quick Start

### Setup

```bash
# Clone and enter directory
git clone https://github.com/saundersconsult/ExploreMassiveAPI.git
cd ExploreMassiveAPI

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
source venv/bin/activate     # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create `config/massive.env`:

```
MASSIVE_API_KEY=your_api_key_here
MASSIVE_API_URL=https://api.massive.com/v3
EXCHANGE=NASDAQ
```

### Usage

```bash
# Explore available endpoints
python src/api_explorer.py

# Fetch exchange holidays
python src/holiday_fetcher.py --exchange NASDAQ

# Run tests
pytest tests/
```

## API Documentation

- Massive.com Official Docs: https://massive.com/docs
- Massive.com System Status: https://massive.com/system
- Local reference (index): [docs/endpoints-by-category.md](docs/endpoints-by-category.md)
- Per-category references: [docs/stocks.md](docs/stocks.md), [docs/forex.md](docs/forex.md), [docs/crypto.md](docs/crypto.md), [docs/options.md](docs/options.md), [docs/futures.md](docs/futures.md), [docs/benzinga.md](docs/benzinga.md), [docs/technical-indicators.md](docs/technical-indicators.md), [docs/federal.md](docs/federal.md), [docs/universal.md](docs/universal.md)

## Project Structure

```
src/
  api_client.py          # Core API wrapper
  api_explorer.py        # Endpoint discovery tool
  holiday_fetcher.py     # Market holidays integration
  
tests/
  test_api_client.py
  test_holidays.py
  
config/
  massive.env.example    # Template for API credentials
  
docs/
  endpoints-by-category.md  # Index linking to per-category references
  stocks.md                 # Stocks endpoints
  forex.md                  # Forex endpoints
  crypto.md                 # Crypto endpoints
  options.md                # Options endpoints
  futures.md                # Futures endpoints
  benzinga.md               # Benzinga feeds
  technical-indicators.md   # Technical indicators
  federal.md                # Treasury yields
  universal.md              # Universal snapshot
  integration-guide.md      # Integration with Signals-Telegram-MT5
```

## Discovered Endpoints

- `/reference/dividends` - Dividend data
- `/reference/holidays` - Exchange holidays (primary use)
- `/markets/{market}/hours` - Trading hours
- More to explore...

## Integration with Signals-Telegram-MT5

Once holidays API is validated, integrate into main listener:
- Prevent trade execution on market closure days
- Filter news events using holiday calendar
- Sync with existing news blackout framework

## License

MIT

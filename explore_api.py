#!/usr/bin/env python3
"""Interactive Massive.com API explorer - discover available endpoints and data."""

import sys
import json
from src.api_client import MassiveAPIClient
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def pretty_print(data, indent=2):
    """Pretty print JSON data."""
    print(json.dumps(data, indent=indent, default=str))


def main():
    """Main explorer menu."""
    try:
        client = MassiveAPIClient()
        logger.info("✅ Connected to Massive.com API")
    except ValueError as e:
        logger.error(f"❌ Configuration error: {e}")
        return
    
    print("\n" + "=" * 70)
    print("MASSIVE.COM API EXPLORER")
    print("=" * 70)
    
    while True:
        print("\n📊 AVAILABLE OPERATIONS:")
        print("  1. 📅 Get Market Holidays")
        print("  2. 💰 Get Dividends (by ticker)")
        print("  3. 📈 Get Stock Details (by ticker)")
        print("  4. 📊 Search Tickers")
        print("  5. 🔍 Test Custom Endpoint")
        print("  6. ℹ️  API Info")
        print("  7. ❌ Exit")
        
        choice = input("\nSelect option (1-7): ").strip()
        
        if choice == "1":
            try:
                logger.info("\n⏳ Fetching market holidays...")
                holidays = client.get_market_holidays()
                logger.info(f"✅ Found {len(holidays)} holidays\n")
                for holiday in holidays[:10]:
                    print(f"  • {holiday.get('date')} ({holiday.get('exchange')}): {holiday.get('name')} - {holiday.get('status')}")
                if len(holidays) > 10:
                    print(f"\n  ... and {len(holidays) - 10} more")
            except Exception as e:
                logger.error(f"❌ Error: {e}")
        
        elif choice == "2":
            ticker = input("\nEnter stock ticker (e.g., AAPL): ").strip().upper()
            try:
                logger.info(f"\n⏳ Fetching dividends for {ticker}...")
                dividends = client.get_dividends(ticker)
                logger.info(f"✅ Found {len(dividends)} dividend records\n")
                for div in dividends[:5]:
                    ex_date = div.get('ex_dividend_date', 'N/A')
                    amount = div.get('dividend_amount', 'N/A')
                    print(f"  • {ex_date}: ${amount}")
                if len(dividends) > 5:
                    print(f"\n  ... and {len(dividends) - 5} more")
            except Exception as e:
                logger.error(f"❌ Error: {e}")
        
        elif choice == "3":
            ticker = input("\nEnter stock ticker (e.g., AAPL): ").strip().upper()
            try:
                logger.info(f"\n⏳ Fetching details for {ticker}...")
                result = client._make_request(f"/reference/tickers/{ticker}")
                logger.info(f"✅ Ticker details for {ticker}:\n")
                if 'results' in result and result['results']:
                    for item in result['results'][:5]:
                        print(f"\n  Symbol: {item.get('ticker', 'N/A')}")
                        print(f"  Name: {item.get('name', 'N/A')}")
                        print(f"  Type: {item.get('type', 'N/A')}")
                        print(f"  Market: {item.get('market', 'N/A')}")
                    if len(result['results']) > 5:
                        print(f"\n  ... and {len(result['results']) - 5} more results")
            except Exception as e:
                logger.error(f"❌ Error: {e}")
        
        elif choice == "4":
            query = input("\nEnter search query (e.g., 'AAPL' or 'apple'): ").strip()
            try:
                logger.info(f"\n⏳ Searching for '{query}'...")
                result = client._make_request("/reference/tickers", params={"search": query, "limit": 10})
                logger.info(f"✅ Search results:\n")
                if 'results' in result and result['results']:
                    for item in result['results']:
                        print(f"  • {item.get('ticker', 'N/A')}: {item.get('name', 'N/A')}")
                    logger.info(f"\nFound {result.get('count', len(result['results']))} results")
                else:
                    logger.warning("No results found")
            except Exception as e:
                logger.error(f"❌ Error: {e}")
        
        elif choice == "5":
            endpoint = input("\nEnter endpoint path (e.g., /query/tickers): ").strip()
            method = input("Enter HTTP method (GET/POST) [GET]: ").strip().upper() or "GET"
            try:
                logger.info(f"\n⏳ Testing {method} {endpoint}...")
                result = client._make_request(endpoint, method=method)
                logger.info(f"✅ Response:\n")
                pretty_print(result)
            except Exception as e:
                logger.error(f"❌ Error: {e}")
        
        elif choice == "6":
            print("\n" + "=" * 70)
            print("API INFORMATION")
            print("=" * 70)
            print(f"Base URL: {client.base_url}")
            print(f"API Key: {client.api_key[:10]}...{'*' * 10}")
            print("\n✅ AVAILABLE ENDPOINTS:")
            print("  • GET /reference/dividends?ticker=AAPL - Dividend history")
            print("  • GET /reference/tickers - Search tickers (with optional 'search' param)")
            print("  • GET /reference/tickers/{TICKER} - Get specific ticker details")
            print("\nNote: Use the menu options above to explore these endpoints!")
        
        elif choice == "7":
            logger.info("\n👋 Goodbye!")
            break
        
        else:
            logger.warning("❌ Invalid option, please try again")


if __name__ == "__main__":
    main()

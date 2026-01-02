"""Interactive explorer for Massive.com API endpoints."""

import logging
from api_client import MassiveAPIClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def explore_endpoints():
    """Interactively explore Massive.com API endpoints."""
    try:
        client = MassiveAPIClient()
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        return
    
    print("=" * 60)
    print("Massive.com API Explorer")
    print("=" * 60)
    
    while True:
        print("\nAvailable commands:")
        print("  1. List known endpoints")
        print("  2. Test holidays endpoint")
        print("  3. Test dividends endpoint")
        print("  4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == "1":
            print("\nKnown endpoints:")
            for endpoint in client.list_endpoints():
                print(f"  - {endpoint}")
        
        elif choice == "2":
            exchange = input("Enter exchange code (NASDAQ, NYSE, AMEX): ").strip()
            try:
                holidays = client.get_holidays(exchange)
                print(f"\nFound {len(holidays)} holidays for {exchange}:")
                for holiday in holidays[:5]:  # Show first 5
                    print(f"  - {holiday}")
                if len(holidays) > 5:
                    print(f"  ... and {len(holidays) - 5} more")
            except Exception as e:
                logger.error(f"Error fetching holidays: {e}")
        
        elif choice == "3":
            ticker = input("Enter stock ticker (e.g., AAPL): ").strip()
            try:
                dividends = client.get_dividends(ticker)
                print(f"\nFound {len(dividends)} dividend records for {ticker}:")
                for div in dividends[:5]:  # Show first 5
                    print(f"  - {div}")
                if len(dividends) > 5:
                    print(f"  ... and {len(dividends) - 5} more")
            except Exception as e:
                logger.error(f"Error fetching dividends: {e}")
        
        elif choice == "4":
            print("\nExiting.")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    explore_endpoints()

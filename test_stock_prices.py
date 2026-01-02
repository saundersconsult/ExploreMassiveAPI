#!/usr/bin/env python3
"""Test stock price and quote endpoints from Massive API."""

from src.api_client import MassiveAPIClient
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def test_endpoint(client, endpoint, description=""):
    """Test an endpoint and report results."""
    try:
        result = client._make_request(endpoint)
        logger.info(f"✅ {description}")
        if isinstance(result, dict):
            logger.info(f"   Response keys: {list(result.keys())}")
            if 'results' in result:
                logger.info(f"   Sample: {str(result['results'])[:100]}")
        return True
    except Exception as e:
        logger.error(f"❌ {description}")
        logger.error(f"   Error: {str(e)[:80]}")
        return False


def main():
    """Test stock price endpoints."""
    try:
        client = MassiveAPIClient()
        logger.info("✅ Connected to Massive.com API\n")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        return
    
    print("=" * 70)
    print("TESTING STOCK PRICE & QUOTE ENDPOINTS")
    print("=" * 70 + "\n")
    
    print("🔍 LAST TRADE & QUOTES:")
    print("-" * 70)
    test_endpoint(client, "/v2/last/trade/AAPL", "Last Trade (AAPL)")
    test_endpoint(client, "/v2/last/nbbo/AAPL", "Last Quote/NBBO (AAPL)")
    
    print("\n🔍 DAILY AGGREGATES:")
    print("-" * 70)
    test_endpoint(client, "/v1/open-close/AAPL/2024-12-31", "Daily Open/Close (AAPL)")
    test_endpoint(client, "/v2/aggs/ticker/AAPL/prev", "Previous Close (AAPL)")
    
    print("\n🔍 SNAPSHOTS:")
    print("-" * 70)
    test_endpoint(client, "/v2/snapshot/locale/us/markets/stocks/tickers", 
                 "Snapshot All Tickers")
    test_endpoint(client, "/v2/snapshot/locale/us/markets/stocks/gainers", 
                 "Snapshot Gainers")
    test_endpoint(client, "/v2/snapshot/locale/us/markets/stocks/losers", 
                 "Snapshot Losers")
    
    print("\n" + "=" * 70)
    logger.info("Stock endpoint testing complete!")


if __name__ == "__main__":
    main()

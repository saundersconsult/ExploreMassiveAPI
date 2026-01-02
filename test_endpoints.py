#!/usr/bin/env python3
"""Test Massive.com API endpoints to discover available data."""

import sys
from src.api_client import MassiveAPIClient
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def test_endpoint(client, endpoint, method="GET", params=None, description=""):
    """Test an endpoint and report results."""
    try:
        result = client._make_request(endpoint, method=method, params=params)
        logger.info(f"✅ {description}")
        logger.info(f"   Endpoint: {endpoint}")
        logger.info(f"   Response keys: {list(result.keys())}")
        if isinstance(result, dict) and 'results' in result:
            logger.info(f"   Results count: {len(result['results'])}")
        return True
    except Exception as e:
        logger.error(f"❌ {description}")
        logger.error(f"   Endpoint: {endpoint}")
        logger.error(f"   Error: {str(e)[:100]}")
        return False


def main():
    """Test various endpoints."""
    try:
        client = MassiveAPIClient()
        logger.info("✅ Connected to Massive.com API\n")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        return
    
    print("=" * 70)
    print("TESTING MASSIVE.COM API ENDPOINTS")
    print("=" * 70 + "\n")
    
    # Test known working endpoints
    print("🔍 Testing KNOWN endpoints:")
    print("-" * 70)
    test_endpoint(client, "/v1/marketstatus/upcoming", 
                 description="Market Holidays (v1)")
    test_endpoint(client, "/reference/dividends", 
                 params={"ticker": "AAPL"},
                 description="Dividends (AAPL)")
    
    print("\n🔍 Testing COMMON endpoints:")
    print("-" * 70)
    
    # Test various ticker/search endpoints
    endpoints_to_test = [
        ("/query/tickers", "GET", {"search": "AAPL", "limit": 5}, "Ticker Search (v3)"),
        ("/reference/tickers", "GET", {"search": "AAPL", "limit": 5}, "Reference Tickers"),
        ("/reference/tickers/AAPL", "GET", None, "Ticker Details (AAPL)"),
        ("/stocks/AAPL", "GET", None, "Stock Info (AAPL)"),
        ("/query/stocks", "GET", {"search": "AAPL"}, "Stock Search"),
    ]
    
    for endpoint, method, params, desc in endpoints_to_test:
        test_endpoint(client, endpoint, method=method, params=params, description=desc)
    
    print("\n🔍 Testing DATA endpoints:")
    print("-" * 70)
    
    data_endpoints = [
        ("/reference/earnings", "GET", {"ticker": "AAPL"}, "Earnings (AAPL)"),
        ("/aggs/ticker/AAPL/range/1/day/2024-01-01/2024-12-31", "GET", None, "Aggregates (AAPL daily)"),
        ("/aggs/ticker/AAPL/prev", "GET", None, "Previous Close (AAPL)"),
        ("/snapshot/locale/us/markets/stocks/tickers/AAPL", "GET", None, "Snapshot (AAPL)"),
    ]
    
    for endpoint, method, params, desc in data_endpoints:
        test_endpoint(client, endpoint, method=method, params=params, description=desc)
    
    print("\n" + "=" * 70)
    logger.info("Test complete! Check results above for available endpoints.")


if __name__ == "__main__":
    main()

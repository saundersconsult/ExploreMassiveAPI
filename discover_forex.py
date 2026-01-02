#!/usr/bin/env python3
"""Discover Massive.com Forex API endpoints."""

from src.api_client import MassiveAPIClient
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def test_forex_endpoint(client, endpoint, params=None, description=""):
    """Test a forex endpoint."""
    try:
        result = client._make_request(endpoint, params=params)
        logger.info(f"✅ {description}")
        logger.info(f"   Endpoint: {endpoint}")
        if isinstance(result, dict):
            logger.info(f"   Response keys: {list(result.keys())}")
            if 'results' in result and result['results']:
                if isinstance(result['results'], list):
                    logger.info(f"   Found {len(result['results'])} results")
                    if result['results'] and isinstance(result['results'][0], dict):
                        logger.info(f"   Sample keys: {list(result['results'][0].keys())[:5]}")
                elif isinstance(result['results'], dict):
                    logger.info(f"   Results (dict): {list(result['results'].keys())[:5]}")
        return True
    except Exception as e:
        logger.error(f"❌ {description}")
        logger.error(f"   Endpoint: {endpoint}")
        logger.error(f"   Error: {str(e)[:80]}")
        return False


def main():
    """Test forex endpoints."""
    try:
        client = MassiveAPIClient()
        logger.info("✅ Connected to Massive.com API\n")
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        return
    
    print("=" * 70)
    print("TESTING FOREX ENDPOINTS")
    print("=" * 70 + "\n")
    
    print("🔍 FOREX TICKERS & REFERENCE:")
    print("-" * 70)
    test_forex_endpoint(client, "/reference/tickers", 
                       params={"market": "fx", "limit": 5},
                       description="List Forex Tickers (market=fx)")
    
    print("\n🔍 FOREX QUOTES & PRICING:")
    print("-" * 70)
    test_forex_endpoint(client, "/quotes/forex/EURUSD", 
                       description="Forex Quote (EURUSD)")
    
    test_forex_endpoint(client, "/forex/snapshot", 
                       params={"ticker": "EURUSD"},
                       description="Forex Snapshot (EURUSD)")
    
    test_forex_endpoint(client, "/forex/EURUSD/quote", 
                       description="Forex Latest Quote (EURUSD)")
    
    test_forex_endpoint(client, "/snapshot/locale/global/markets/forex/tickers/EURUSD", 
                       description="Forex Snapshot (alternate path)")
    
    print("\n🔍 FOREX AGGREGATES & HISTORICAL DATA:")
    print("-" * 70)
    test_forex_endpoint(client, "/aggs/ticker/EURUSD/range/1/day/2024-01-01/2024-12-31", 
                       description="Daily Aggregates (EURUSD)")
    
    test_forex_endpoint(client, "/forex/EURUSD/agg/1/day/2024-01-01/2024-12-31", 
                       description="Daily Aggregates (EURUSD - alternate)")
    
    test_forex_endpoint(client, "/aggs/ticker/EURUSD/prev", 
                       description="Previous Close (EURUSD)")
    
    print("\n🔍 FOREX REAL-TIME DATA:")
    print("-" * 70)
    test_forex_endpoint(client, "/forex/EURUSD/real-time", 
                       description="Real-time Forex (EURUSD)")
    
    print("\n" + "=" * 70)
    logger.info("Forex endpoint discovery complete!")
    logger.info("Check endpoints marked ✅ for available data.")


if __name__ == "__main__":
    main()

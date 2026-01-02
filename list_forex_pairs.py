#!/usr/bin/env python3
"""List available Forex currency pairs."""

from src.api_client import MassiveAPIClient

client = MassiveAPIClient()
result = client._make_request('/reference/tickers', params={'market': 'fx', 'limit': 50})

print("\n" + "=" * 70)
print("MASSIVE.COM FOREX - AVAILABLE CURRENCY PAIRS")
print("=" * 70 + "\n")

if result.get('results'):
    print(f"📊 Showing {len(result['results'])} of {result.get('count', '?')} available pairs:\n")
    for ticker in result['results']:
        print(f"  • {ticker['ticker']}: {ticker['name']}")
    
    if result.get('count', 0) > 50:
        print(f"\n✅ Total pairs available: {result.get('count')} (pagination available)")

print("\n" + "=" * 70)

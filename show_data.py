#!/usr/bin/env python3
"""Simple Massive.com API data explorer (respects 5 calls/min rate limit)."""

from src.api_client import MassiveAPIClient
import json

def main():
    client = MassiveAPIClient()
    print("✅ Connected to Massive.com API")
    print("📋 Rate limit: 5 calls per minute\n")
    
    print("=" * 70)
    print("MASSIVE.COM API - AVAILABLE DATA")
    print("=" * 70)
    
    # Test 1: Dividends
    print("\n1️⃣  DIVIDEND DATA (AAPL)")
    print("-" * 70)
    dividends = client.get_dividends("AAPL")
    print(f"✅ Found {len(dividends)} dividend records\n")
    for div in dividends[:5]:
        amount = div.get('cash_amount') or div.get('dividend_amount')
        print(f"  • {div.get('ex_dividend_date')}: ${amount}")
    if len(dividends) > 5:
        print(f"  ... and {len(dividends) - 5} more")
    
    # Test 2: Ticker Search
    print("\n2️⃣  SEARCH TICKERS ('APPLE')")
    print("-" * 70)
    tickers = client._make_request("/reference/tickers", params={"search": "APPLE", "limit": 5})
    print(f"✅ Found {len(tickers.get('results', []))} results\n")
    for ticker in tickers.get('results', [])[:5]:
        print(f"  • {ticker.get('ticker')}: {ticker.get('name')}")
    
    # Test 3: Get MSFT dividends
    print("\n3️⃣  DIVIDEND DATA (MSFT)")
    print("-" * 70)
    msft_divs = client.get_dividends("MSFT")
    print(f"✅ Found {len(msft_divs)} dividend records\n")
    for div in msft_divs[:5]:
        amount = div.get('cash_amount') or div.get('dividend_amount')
        print(f"  • {div.get('ex_dividend_date')}: ${amount}")
    if len(msft_divs) > 5:
        print(f"  ... and {len(msft_divs) - 5} more")
    
    # Test 4: Search NVIDIA
    print("\n4️⃣  SEARCH TICKERS ('NVIDIA')")
    print("-" * 70)
    nvda = client._make_request("/reference/tickers", params={"search": "NVIDIA", "limit": 5})
    print(f"✅ Found {len(nvda.get('results', []))} results\n")
    for ticker in nvda.get('results', [])[:5]:
        print(f"  • {ticker.get('ticker')}: {ticker.get('name')}")
    
    # Test 5: Get TSLA dividends
    print("\n5️⃣  DIVIDEND DATA (TSLA)")
    print("-" * 70)
    tsla_divs = client.get_dividends("TSLA")
    print(f"✅ Found {len(tsla_divs)} dividend records\n")
    if tsla_divs:
        for div in tsla_divs[:5]:
            amount = div.get('cash_amount') or div.get('dividend_amount')
            print(f"  • {div.get('ex_dividend_date')}: ${amount}")
        if len(tsla_divs) > 5:
            print(f"  ... and {len(tsla_divs) - 5} more")
    else:
        print("  (No dividend records found)")
    
    print("\n" + "=" * 70)
    print("✅ Data exploration complete!")
    print("=" * 70)
    
    print("=" * 70)
    print("✅ Data exploration complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()

"""Core Massive.com API client wrapper."""

import os
import requests
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
import logging
import time
from collections import deque

logger = logging.getLogger(__name__)


class RateLimiter:
    """Rate limiter for API calls (5 per minute)."""
    
    def __init__(self, calls_per_minute: int = 5):
        self.calls_per_minute = calls_per_minute
        self.min_interval = 60 / calls_per_minute  # 12 seconds per call
        self.call_times = deque(maxlen=calls_per_minute)
    
    def wait_if_needed(self):
        """Wait if necessary to respect rate limit."""
        if len(self.call_times) < self.calls_per_minute:
            # Haven't hit limit yet
            self.call_times.append(time.time())
            return
        
        # Check if oldest call is outside the window
        oldest = self.call_times[0]
        now = time.time()
        time_since_oldest = now - oldest
        
        if time_since_oldest < 60:
            wait_time = 60 - time_since_oldest + 0.1
            logger.info(f"⏳ Rate limit: waiting {wait_time:.1f}s...")
            time.sleep(wait_time)
        
        self.call_times.append(time.time())


class MassiveAPIClient:
    """Wrapper for Massive.com API endpoints."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """Initialize API client.
        
        Args:
            api_key: API key (defaults to MASSIVE_API_KEY env var)
            base_url: Base API URL (defaults to MASSIVE_API_URL env var)
        """
        load_dotenv("config/massive.env")
        
        self.api_key = api_key or os.getenv("MASSIVE_API_KEY")
        self.base_url = base_url or os.getenv("MASSIVE_API_URL", "https://api.massive.com/v3")
        
        if not self.api_key:
            raise ValueError("MASSIVE_API_KEY not configured. Set in config/massive.env or pass as argument.")
        
        self.session = requests.Session()
        self.rate_limiter = RateLimiter(calls_per_minute=5)
        self._setup_headers()
    
    def _setup_headers(self):
        """Configure default headers for API requests."""
        self.session.headers.update({
            "User-Agent": "ExploreMassiveAPI/0.1.0",
            "Accept": "application/json"
        })
    
    def _make_request(self, endpoint: str, method: str = "GET", 
                     params: Optional[Dict[str, Any]] = None,
                     data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make HTTP request to API endpoint.
        
        Args:
            endpoint: API endpoint (e.g., "/reference/holidays")
            method: HTTP method
            params: Query parameters
            data: Request body data
            
        Returns:
            Response JSON
        """
        # Respect rate limit
        self.rate_limiter.wait_if_needed()
        
        url = f"{self.base_url}{endpoint}"
        
        # Add API key to params
        if params is None:
            params = {}
        params["apiKey"] = self.api_key
        
        try:
            response = self.session.request(method, url, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            raise
    
    def get_market_holidays(self) -> List[Dict[str, Any]]:
        """Fetch upcoming market holidays and their trading status.
        
        This endpoint returns TRADING market closures and early closes, not all holidays.
        Filters include: Thanksgiving, Christmas, Independence Day, etc.
        
        Returns:
            List of market holiday dictionaries with structure:
            {
                "date": "2020-11-26",
                "exchange": "NYSE",
                "name": "Thanksgiving",
                "status": "closed" | "early-close",
                "open": "2020-11-27T14:30:00.000Z" (if early-close),
                "close": "2020-11-27T18:00:00.000Z" (if early-close)
            }
        """
        # Note: This endpoint is at /v1/, not /v3/
        url = f"{self.base_url.replace('/v3', '/v1')}/marketstatus/upcoming"
        params = {"apiKey": self.api_key}
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json() if isinstance(response.json(), list) else response.json().get("results", [])
        except Exception as e:
            logger.error(f"API request failed: {e}")
            raise
    
    def get_dividends(self, ticker: str) -> List[Dict[str, Any]]:
        """Fetch dividend history for a ticker.
        
        Args:
            ticker: Stock ticker symbol
            
        Returns:
            List of dividend records
        """
        response = self._make_request("/reference/dividends", params={"ticker": ticker})
        return response.get("results", [])
    
    def list_endpoints(self) -> List[str]:
        """List available endpoints discovered so far.
        
        Returns:
            List of known endpoints
        """
        return [
            "/reference/holidays",
            "/reference/dividends",
            "/markets/{market}/hours",
            # Add more as discovered
        ]
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

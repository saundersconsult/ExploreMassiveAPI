"""Core Massive.com API client wrapper."""

import os
import requests
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)


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
    
    def get_holidays(self, exchange: str) -> List[Dict[str, Any]]:
        """Fetch holidays for an exchange.
        
        NOTE: Massive.com API does not currently expose a holidays endpoint.
        See holiday_fetcher.py for alternative approaches:
        - External calendar APIs (ICS files, Google Calendar API)
        - Manual holiday mapping
        - Integration with broker holiday calendars (MT5, etc.)
        
        Args:
            exchange: Exchange code (NASDAQ, NYSE, etc.)
            
        Returns:
            List of holiday dictionaries (currently empty)
        """
        # TODO: Implement alternative holiday source
        # Options:
        # 1. Scrape from NASDAQ/NYSE websites
        # 2. Use third-party API (e.g., holidays.gov, Google Calendar)
        # 3. Maintain hardcoded list
        # 4. Parse ICS files from exchanges
        logger.warning("Holidays endpoint not available in Massive.com API; returning empty list")
        return []
    
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

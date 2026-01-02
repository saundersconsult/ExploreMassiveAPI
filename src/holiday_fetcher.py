"""Market holiday fetcher for trade blocking."""

import logging
from datetime import datetime, date
from typing import List, Set, Optional
from api_client import MassiveAPIClient

logger = logging.getLogger(__name__)


class HolidayFetcher:
    """Fetches and caches market holidays to prevent trading."""
    
    def __init__(self, exchange: str = "NASDAQ"):
        """Initialize holiday fetcher.
        
        Args:
            exchange: Default exchange code
        """
        self.exchange = exchange
        self.client = MassiveAPIClient()
        self._cache: Optional[Set[date]] = None
        self._cache_timestamp: Optional[datetime] = None
    
    def fetch_holidays(self, exchange: Optional[str] = None, force_refresh: bool = False) -> Set[date]:
        """Fetch holidays for exchange.
        
        Args:
            exchange: Exchange code (uses default if not specified)
            force_refresh: Force cache refresh
            
        Returns:
            Set of holiday dates
        """
        exchange = exchange or self.exchange
        
        if self._cache and not force_refresh:
            return self._cache
        
        try:
            holidays_data = self.client.get_holidays(exchange)
            holiday_dates = set()
            
            for holiday in holidays_data:
                # Parse date from response
                # Adjust based on actual API response format
                try:
                    holiday_date = datetime.fromisoformat(holiday.get("date")).date()
                    holiday_dates.add(holiday_date)
                except (ValueError, TypeError, KeyError):
                    logger.warning(f"Could not parse holiday: {holiday}")
            
            self._cache = holiday_dates
            self._cache_timestamp = datetime.now()
            logger.info(f"Cached {len(holiday_dates)} holidays for {exchange}")
            
            return holiday_dates
        
        except Exception as e:
            logger.error(f"Error fetching holidays for {exchange}: {e}")
            return set()
    
    def is_holiday(self, check_date: Optional[date] = None, exchange: Optional[str] = None) -> bool:
        """Check if a date is a market holiday.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            
        Returns:
            True if date is a holiday
        """
        check_date = check_date or date.today()
        holidays = self.fetch_holidays(exchange)
        return check_date in holidays
    
    def get_next_trading_day(self, start_date: Optional[date] = None, 
                            exchange: Optional[str] = None) -> date:
        """Get next trading day after start date.
        
        Args:
            start_date: Start date (uses today if not specified)
            exchange: Exchange code
            
        Returns:
            Next trading day
        """
        from datetime import timedelta
        
        start_date = start_date or date.today()
        holidays = self.fetch_holidays(exchange)
        
        current = start_date + timedelta(days=1)
        while current.weekday() >= 5 or current in holidays:  # 5=Saturday, 6=Sunday
            current += timedelta(days=1)
        
        return current


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    fetcher = HolidayFetcher("NASDAQ")
    
    # Test fetch
    holidays = fetcher.fetch_holidays()
    print(f"Found {len(holidays)} holidays")
    
    # Test check
    if fetcher.is_holiday():
        print("Today is a market holiday")
    else:
        print("Today is a trading day")
    
    # Test next trading day
    next_trading = fetcher.get_next_trading_day()
    print(f"Next trading day: {next_trading}")

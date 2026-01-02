"""Market holiday fetcher using Massive.com API."""

import logging
from datetime import datetime, date, timedelta
from typing import List, Optional, Dict, Any
from api_client import MassiveAPIClient

logger = logging.getLogger(__name__)


class HolidayFetcher:
    """Fetches and caches trading market holidays from Massive.com API.
    
    Returns ACTUAL TRADING HOLIDAYS (closed/early-close), not all calendar holidays.
    Examples: Thanksgiving, Christmas, Independence Day (market closures only)
    """
    
    def __init__(self, exchange: str = "NASDAQ"):
        """Initialize holiday fetcher.
        
        Args:
            exchange: Default exchange code (NASDAQ, NYSE, etc.)
        """
        self.exchange = exchange
        self.client = MassiveAPIClient()
        self._cache: Optional[List[Dict[str, Any]]] = None
        self._cache_timestamp: Optional[datetime] = None
        self._cache_duration = timedelta(hours=24)  # Refresh daily
    
    def fetch_holidays(self, exchange: Optional[str] = None, 
                      force_refresh: bool = False) -> List[Dict[str, Any]]:
        """Fetch upcoming market holidays from Massive.com API.
        
        Returns actual trading holidays (closed/early-close status) for specific exchange.
        
        Args:
            exchange: Exchange code (NASDAQ, NYSE, etc.) - filters results
            force_refresh: Force cache refresh
            
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
        exchange = exchange or self.exchange
        
        # Check cache validity
        if self._cache and not force_refresh:
            if datetime.now() - self._cache_timestamp < self._cache_duration:
                return self._filter_by_exchange(self._cache, exchange)
        
        try:
            all_holidays = self.client.get_market_holidays()
            self._cache = all_holidays
            self._cache_timestamp = datetime.now()
            
            filtered = self._filter_by_exchange(all_holidays, exchange)
            logger.info(f"Cached {len(all_holidays)} market holidays; {len(filtered)} for {exchange}")
            
            return filtered
        
        except Exception as e:
            logger.error(f"Error fetching market holidays: {e}")
            return []
    
    def _filter_by_exchange(self, holidays: List[Dict[str, Any]], 
                           exchange: str) -> List[Dict[str, Any]]:
        """Filter holidays to specific exchange."""
        return [h for h in holidays if h.get("exchange") == exchange]
    
    def is_market_closed(self, check_date: Optional[date] = None, 
                        exchange: Optional[str] = None) -> bool:
        """Check if market is completely closed on a date.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            
        Returns:
            True if market has "closed" status (not early-close)
        """
        check_date = check_date or date.today()
        exchange = exchange or self.exchange
        
        holidays = self.fetch_holidays(exchange)
        date_str = check_date.isoformat()
        
        for holiday in holidays:
            if holiday.get("date") == date_str and holiday.get("status") == "closed":
                return True
        
        return False
    
    def is_early_close(self, check_date: Optional[date] = None, 
                      exchange: Optional[str] = None) -> bool:
        """Check if market has early close on a date.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            
        Returns:
            True if market has "early-close" status
        """
        check_date = check_date or date.today()
        exchange = exchange or self.exchange
        
        holidays = self.fetch_holidays(exchange)
        date_str = check_date.isoformat()
        
        for holiday in holidays:
            if holiday.get("date") == date_str and holiday.get("status") == "early-close":
                return True
        
        return False
    
    def get_holiday_info(self, check_date: Optional[date] = None, 
                        exchange: Optional[str] = None) -> Optional[Dict[str, Any]]:
        """Get complete holiday details for a date.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            
        Returns:
            Full holiday dictionary if date is a holiday, None otherwise
            Includes: date, name, status, open time (if early-close), close time
        """
        check_date = check_date or date.today()
        exchange = exchange or self.exchange
        
        holidays = self.fetch_holidays(exchange)
        date_str = check_date.isoformat()
        
        for holiday in holidays:
            if holiday.get("date") == date_str:
                return holiday
        
        return None
    
    def is_trading_day(self, check_date: Optional[date] = None, 
                      exchange: Optional[str] = None, 
                      exclude_weekends: bool = True) -> bool:
        """Check if a date is a regular/normal trading day.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            exclude_weekends: Exclude weekends from trading days
            
        Returns:
            True if market is open for normal trading (not closed)
            Note: Early-close days return True (market is still open)
        """
        check_date = check_date or date.today()
        
        if exclude_weekends and check_date.weekday() >= 5:  # Saturday=5, Sunday=6
            return False
        
        return not self.is_market_closed(check_date, exchange)
    
    def get_early_close_time(self, check_date: Optional[date] = None, 
                            exchange: Optional[str] = None) -> Optional[str]:
        """Get early close time if market closes early on this date.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            
        Returns:
            Close time in ISO format (e.g., "2020-11-27T18:00:00.000Z") if early close,
            None otherwise
        """
        holiday_info = self.get_holiday_info(check_date, exchange)
        if holiday_info and holiday_info.get("status") == "early-close":
            return holiday_info.get("close")
        return None
    
    def get_holiday_name(self, check_date: Optional[date] = None, 
                        exchange: Optional[str] = None) -> Optional[str]:
        """Get the name of the holiday if this date is a market holiday.
        
        Args:
            check_date: Date to check (uses today if not specified)
            exchange: Exchange code (uses default if not specified)
            
        Returns:
            Holiday name (e.g., "Thanksgiving", "Christmas") or None
        """
        holiday_info = self.get_holiday_info(check_date, exchange)
        return holiday_info.get("name") if holiday_info else None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    fetcher = HolidayFetcher("NASDAQ")
    
    # Fetch holidays
    print("\n📅 Upcoming market holidays for NASDAQ:")
    holidays_list = fetcher.fetch_holidays()
    for h in holidays_list[:5]:
        status_emoji = "🔴" if h['status'] == 'closed' else "⏱️"
        print(f"  {status_emoji} {h['date']}: {h['name']} - {h['status']}")
    
    # Test current date
    print(f"\n📊 Today ({date.today()}):")
    if fetcher.is_market_closed():
        print(f"  ❌ Market CLOSED ({fetcher.get_holiday_name()})")
    elif fetcher.is_early_close():
        close_time = fetcher.get_early_close_time()
        print(f"  ⏱️  EARLY CLOSE at {close_time}")
    else:
        print(f"  ✅ Regular trading day")


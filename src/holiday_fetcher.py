"""Market holiday fetcher for trade blocking."""

import logging
from datetime import datetime, date, timedelta
from typing import Set, Optional

try:
    import holidays
except ImportError:
    raise ImportError(
        "holidays package not installed. Install with: pip install holidays"
    )

logger = logging.getLogger(__name__)


class HolidayFetcher:
    """Fetches and caches US market holidays to prevent trading."""
    
    def __init__(self, exchange: str = "NASDAQ"):
        """Initialize holiday fetcher.
        
        Args:
            exchange: Exchange code (NASDAQ, NYSE, etc.)
                     Note: holidays package uses US market holidays only
        """
        self.exchange = exchange
        self._cache: Optional[Set[date]] = None
        self._cache_year: Optional[int] = None
    
    def fetch_holidays(self, year: Optional[int] = None, force_refresh: bool = False) -> Set[date]:
        """Fetch US market holidays for a given year.
        
        Args:
            year: Year to fetch (defaults to current year)
            force_refresh: Force cache refresh
            
        Returns:
            Set of holiday dates
        """
        year = year or datetime.now().year
        
        # Return cached value if year matches and not forcing refresh
        if self._cache and self._cache_year == year and not force_refresh:
            return self._cache
        
        try:
            # Get US holidays for the year
            us_holidays = holidays.US(years=year)
            
            # Convert to set of dates
            holiday_dates = set(us_holidays.keys())
            
            self._cache = holiday_dates
            self._cache_year = year
            
            logger.info(f"Cached {len(holiday_dates)} US holidays for {year}")
            
            return holiday_dates
        
        except Exception as e:
            logger.error(f"Error fetching holidays: {e}")
            return set()
    
    def is_holiday(self, check_date: Optional[date] = None) -> bool:
        """Check if a date is a US market holiday.
        
        Args:
            check_date: Date to check (uses today if not specified)
            
        Returns:
            True if date is a holiday
        """
        check_date = check_date or date.today()
        holidays_set = self.fetch_holidays(check_date.year)
        return check_date in holidays_set
    
    def is_trading_day(self, check_date: Optional[date] = None) -> bool:
        """Check if a date is a trading day (not weekend or holiday).
        
        Args:
            check_date: Date to check (uses today if not specified)
            
        Returns:
            True if date is a trading day
        """
        check_date = check_date or date.today()
        
        # Check if weekend (Monday=0, Sunday=6)
        if check_date.weekday() >= 5:  # Saturday or Sunday
            return False
        
        # Check if holiday
        if self.is_holiday(check_date):
            return False
        
        return True
    
    def get_next_trading_day(self, start_date: Optional[date] = None) -> date:
        """Get next trading day after start date.
        
        Args:
            start_date: Start date (uses today if not specified)
            
        Returns:
            Next trading day
        """
        start_date = start_date or date.today()
        current = start_date + timedelta(days=1)
        
        while not self.is_trading_day(current):
            current += timedelta(days=1)
        
        return current
    
    def get_holiday_name(self, check_date: Optional[date] = None) -> Optional[str]:
        """Get the name of a holiday if date is a holiday.
        
        Args:
            check_date: Date to check (uses today if not specified)
            
        Returns:
            Holiday name or None if not a holiday
        """
        check_date = check_date or date.today()
        
        try:
            us_holidays = holidays.US(years=check_date.year)
            return us_holidays.get(check_date)
        except Exception as e:
            logger.error(f"Error getting holiday name: {e}")
            return None


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    fetcher = HolidayFetcher("NASDAQ")
    
    # Test fetch
    holidays_set = fetcher.fetch_holidays()
    print(f"Found {len(holidays_set)} holidays this year")
    print(f"First 5 holidays: {sorted(list(holidays_set))[:5]}")
    
    # Test check
    today = date.today()
    if fetcher.is_holiday(today):
        print(f"\n{today} is a market holiday: {fetcher.get_holiday_name(today)}")
    else:
        print(f"\n{today} is a trading day")
    
    # Test next trading day
    next_trading = fetcher.get_next_trading_day()
    print(f"Next trading day: {next_trading}")
    
    # Test with specific dates
    print("\nTesting specific dates:")
    test_dates = [
        date(2026, 1, 1),   # New Year's Day
        date(2026, 1, 20),  # MLK Day
        date(2026, 1, 5),   # Regular trading day
    ]
    
    for test_date in test_dates:
        trading = fetcher.is_trading_day(test_date)
        holiday_name = fetcher.get_holiday_name(test_date)
        status = f"Holiday: {holiday_name}" if holiday_name else "Trading day"
        print(f"  {test_date}: {status}")


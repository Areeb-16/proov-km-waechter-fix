# fleet_utils.py
# Catch-all helpers since 2013.

MILES_PER_KM = 0.621371                 # 1 km = 0.621371 miles (corrected from 1.609)


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles. Used by the nightly UK partner report."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"

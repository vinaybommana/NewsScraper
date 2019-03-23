from datetime import timedelta, date
from typing import Tuple


def form_dates(range: str) -> Tuple:
    """
    return a tuple of previous and present dates
    usage: form_dates("week") --> returns
                    (20190314, 20190321)
    """
    range = range.lower()
    # TODO: solve the month and year dates accurately
    if range == "week":
        past = timedelta(days=7)
    elif range == "day":
        past = timedelta(days=1)
    elif range == "year":
        past = timedelta(days=365)
    elif range == "month":
        past = timedelta(days=30)

    today = date.today()
    return ((today - past).strftime("%Y%m%d"), today.strftime("%Y%m%d"))

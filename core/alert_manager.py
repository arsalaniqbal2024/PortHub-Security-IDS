import time

from config import ALERT_COOLDOWN
from core.tracker import last_alert_time


def can_alert(key):
    """
    Determine whether an alert should be generated.

    This function prevents duplicate alerts from being generated
    within the configured cooldown period.

    Args:
        key (str): Unique identifier for an alert source.

    Returns:
        bool:
            True if a new alert is allowed.
            False if the alert is still within the cooldown period.
    """

    current_time = time.time()

    last_time = last_alert_time.get(key)

    # First occurrence of this alert
    if last_time is None:
        last_alert_time[key] = current_time
        return True

    # Cooldown has expired
    if current_time - last_time >= ALERT_COOLDOWN:
        last_alert_time[key] = current_time
        return True

    # Duplicate alert within cooldown period
    return False

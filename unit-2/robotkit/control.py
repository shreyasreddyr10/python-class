"""Movement decisions for robotkit."""
from robotkit import sensors as _sensors
def decide(distance):
    """Return STOP, SLOW or GO for a distance in centimetres."""
    if distance < _sensors.STOP_CM:
        return "STOP"
    elif distance < _sensors.SLOW_CM:
        return "SLOW"
    return "GO"
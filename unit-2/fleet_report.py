def battery_band(pct):
    """Return CRITICAL, LOW or OK for a battery percentage."""
    if pct < 15:
        return "CRITICAL"
    elif pct < 30:
        return "LOW"
    return "OK"
fleet = {"Alpha": 8, "Beta": 22, "Gamma": 76, "Delta": 41}
for name, pct in fleet.items():
    print(f"{name:<7} {pct:>3}%  {battery_band(pct)}")
print(battery_band.__doc__)
def band_print(pct):
    """Print the band instead of returning it."""
    if pct < 15:
        print("CRITICAL")
    else:
        print("OK")
result = band_print(8)
print("returned:", result)
print("type    :", type(result))
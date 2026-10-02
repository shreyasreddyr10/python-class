def stats(values):
    """Return mean, minimum and maximum of a list."""
    return sum(values) / len(values), min(values), max(values)
readings = [22.5, 23.1, 21.8, 24.0, 22.9]
mean, lo, hi = stats(readings)
print(f"mean={mean:.2f}  min={lo}  max={hi}")
packed = stats(readings)
print("as a tuple:", packed, type(packed))
def add_reading(data, value):
    """Append a value to the caller's list."""
    data.append(value)
def rebind(data):
    """Rebind the local name and return the new list."""
    data = [99]
    return data
readings1 = [10, 20]
add_reading(readings1, 30)
print("caller list is now:", readings1)
readings2 = [10, 20]
rebind(readings2)
print("caller list unchanged:", readings2)
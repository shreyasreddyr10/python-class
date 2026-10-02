import sensors
readings = [62, 84, 71]
print("threshold:", sensors.THRESHOLD)
print("average  :", sensors.average(readings))
for r in readings:
    print(r, "->", "ALERT" if sensors.is_alert(r) else "ok")
print("__name__ inside main.py is:", __name__)
print("__name__ inside sensors is:", sensors.__name__)
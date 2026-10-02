robot = {"name": "Alpha", "battery": 78, "mode": "auto"}
print(robot)
print(robot["name"])
robot["battery"] -= 5
robot["speed"] = 0.4
print(robot)
print(robot.get("current"))
print(robot.get("current", 0.0))
print("speed" in robot)
log = ["E2", "E7", "E2", "E1", "E7", "E2"]
freq = {}
for code in log:
    freq[code] = freq.get(code, 0) + 1
print(freq)
for code in sorted(freq, key=freq.get, reverse=True):
    print(f"{code} occurred {freq[code]} time(s)")
for key, value in robot.items():
    print(f"{key:<8} {value}")
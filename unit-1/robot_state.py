robot_name = "Alpha"
battery_pct = 78.5
is_docked = True
waypoints = 12
print(robot_name, battery_pct, is_docked, waypoints)
print(type(robot_name), type(battery_pct), type(is_docked), type(waypoints))
battery_pct = 45
if battery_pct < 50:
    print("Charging recommended")
    print("Docking now")
print("Status check done")
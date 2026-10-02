obstacles = [(1, 2), (3, 3), (0, 4)]
for row in range(5):
    for col in range(5):
        if (row, col) in obstacles:
            print("#", end="")
        else:
            print(".", end="")
    print()
readings = [22.5, 23.1, 21.8, 24.0, 22.9]
total = 0
for r in readings:
    total += r
print("sum   :", total)
print("count :", len(readings))
print("mean  :", total / len(readings))
checks = [12, -1, 34, 78, 15]
for r in checks:
    if r < 0:
        continue
    if r > 70:
        print("DANGER at", r)
        break
else:
    print("all readings safe")
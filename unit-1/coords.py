position = (4.2, 7.8)
print(position, type(position))
x, y = position
print("x =", x, "| y =", y)
single = (5,)
print(single, type(single))
visited = {(0, 0), (0, 1)}
visited.add((1, 1))
visited.add((0, 0))
print(visited)
print("count:", len(visited))
print("(1,1) visited?", (1, 1) in visited)
print("(9,9) visited?", (9, 9) in visited)
codes = ["E2", "E7", "E2", "E1", "E7"]
print("raw   :", codes)
print("unique:", set(codes))
print("unique count:", len(set(codes)))
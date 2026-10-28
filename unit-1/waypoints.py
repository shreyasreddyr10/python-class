
route = [(0, 0), (5, 1)]
print(route)
route.append((2, 3))
print("after append :", route)
route.insert(0, (9, 9))
print("after insert :", route)
route.remove((5, 1))
print("after remove :", route)
print("length:", len(route), "| sorted:", sorted(route))
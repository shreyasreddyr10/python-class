class Probe:
    def __init__(self, pid):
        self.pid = pid
        print("Created", self.pid)

    def __del__(self):
        print("Destroyed", self.pid)


p = Probe(1)

q = p

del p

print("q still works:", q.pid)

del q

print("End of demo")
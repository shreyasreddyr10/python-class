class Robot:
    """A mobile robot with a battery."""

    def __init__(self, name, battery=100):
        self.name = name
        self.battery = battery

    def drain(self, amount):
        self.battery = max(0, self.battery - amount)

    def status(self):
        return f"{self.name}:{self.battery}%"


r1 = Robot("Alpha")
r2 = Robot("Beta", 60)

r1.drain(35)

print(r1.status())
print(r2.status())
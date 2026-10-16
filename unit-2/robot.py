from Point import Point

class Robot:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show(self):
        print(f"Robot: {self.name}")
        self.position.display()

p = Point(5, 10)
r = Robot("Robo1", p)
r.show()
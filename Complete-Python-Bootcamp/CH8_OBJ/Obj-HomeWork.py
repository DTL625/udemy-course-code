import math

class Line:
    def __init__(self, cord1, cord2):
        self.cord1 = {
            'x': cord1[0],
            'y': cord1[1]
        }
        self.cord2 = {
            'x': cord2[0],
            'y': cord2[1]
        }

    def distance(self):
        x = self.cord1['x'] - self.cord2['x']
        y = self.cord1['y'] - self.cord2['y']
        summary = (x * x) + (y * y)

        return abs(math.sqrt(summary))

    def slope(self):
        x = self.cord2['x'] - self.cord1['x']
        y = self.cord2['y'] - self.cord1['y']

        return abs(y/x)


cord2 = (3, 2)
cord1 = (8, 10)

li = Line(cord1, cord2)
print("line distance: {}".format(li.distance())) # 9.433981132056603
print("line slope: {}".format(li.slope())) # 1.6


#---------------------------------------------------------------------------

class Cylinder:

    pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):

        return self.radius ** 2 * self.pi * self.height

    def surface_area(self):

        return (self.pi * self.radius **2 );

c = Cylinder(2, 3)
print(f"Cylinder volume: {c.volume()}")
print(f"Cylinder surface_area: {c.surface_area()}")

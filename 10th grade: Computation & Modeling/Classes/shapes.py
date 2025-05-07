class Shape():
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color

    def describe(self):
        print("Base: {}".format(self.base))
        print("Height: {}".format(self.height))
        print("Color: {}".format(self.color))
        print("Perimeter: {}".format(self.perimeter))
        print("Area: {}".format(self.area))
        print("Vertices: {}".format(self.vertices))

    def render(self):

        import matplotlib.pyplot as plt
        plt.style.use('bmh')   
        
        x_coords = [coord[0] for coord in self.vertices] + [self.vertices[0][0]]
        y_coords = [coord[1] for coord in self.vertices] + [self.vertices[0][1]]

        plt.plot(x_coords, y_coords, color = self.color)
        plt.gca().set_aspect("equal")
        correct_name = str(self).split(".")[1].split(" ")[0]
        plt.savefig('{}.png'.format(correct_name))
        plt.clf()

class Rectangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = (2 * self.base) + (2 * self.height)
        self.area = self.base * self.height
        self.vertices = [(0, 0), (self.base, 0), (self.base, self.height), (0, self.height)]

class RightTriangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(base, height, color)
        self.perimeter = self.base + self.height + (((self.base ** 2) + (self.height ** 2)) ** (1/2))
        self.area = (self.base * self.height) / 2
        self.vertices = [(0, 0), (self.base, 0), (0, self.height)]

class Square(Rectangle):
    def __init__(self, base, color):
        super().__init__(base, base, color)

"""
rect = Rectangle(5, 2, 'red')
rect.describe()
rect.render()

tri = RightTriangle(5,2,'blue')
tri.describe()
tri.render()

sq = Square(5, 'green')
sq.describe()
sq.render()
"""
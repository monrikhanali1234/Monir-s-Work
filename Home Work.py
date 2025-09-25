s = 'good morning'
print(s.upper())
print(s.strip())

s = "Hello, World!"
print(s.find("World"))   # Output: 7
print(s.replace("World", "Python"))

s = [
    [45, 86, 78],
    [12, 63, 79],
    [32, 52, 71]
]
print(s[1][1:3], s[2][1:3])

w=[1,2,3,4,14,18,24,25]
s = [x**2 for x in w]
print(s)

r=[x**2 for x in w if x%2==0]
print(r)

nested_tuple = ((5,6),(2,4),(7,1))
#class = function/method,
#variable = instance/class

#task (1-3)
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

r = Rectangle(4,3)
print(r.area())

s = Square(3)
print(s.area())

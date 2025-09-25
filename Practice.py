from email.headerregistry import MessageIDHeader
from pickle import GLOBAL

_var = 12
var = 13
Var = 14
print(Var)

s = "hello python"
print(s)
print(type(s))
i = 12
print(i , type(i))

f = 2.345666
print(f , type(f))
b = True
print(b, type(b))






x = 10
#print(x)
x = 15
x = "hello"
print(x)

x = y = z = 10
print(x,"\n",y,"\n",z)
print(x)

x = 12

def fun():
    x = 15
    print("inside",x)

print("outside",x)
fun()

x = 12

def fun():
    global x
    x = 15
    print("inside",x)

fun()
print("outside",x)

def fun(a):
    return a*a

print(fun(5))


square = lambda x: x ** 2
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)
fi = list(filter(lambda x: x % 2 == 0, numbers ))
print(fi)

from functools import reduce
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce with a lambda function to sum all the numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

# Output the result
print(sum_of_numbers)

class Person:
    special = "special variable"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def rusalt(self):
        print (self.name, self.age)

p=Person("korim", 24)
p.rusalt()
print(p.special)

s = 'rosie'
t = 10
u = 4.57
v = True
print(s, type(s))
print(t, type(t))
print(u, type(u))
print(v, type(v))


x=y=z=100
print('\n',x,'\n',y,"\n",z)


a = 3+9j
print(a, type(a))

s = "Hello, Python"
i = s[0]
print(i)
print(s[5])
print(s[1:4])
print(s[-1])
print(s[7:])
print(s.lower())


His_boyan = 'HEllo Buddies'
i = His_boyan[7:]
print(His_boyan.lower())

PI = 3.14159  # A constant

GRAVITY = 9.8

print(PI, GRAVITY)  # Output: 3.14159 9.8

a = 5

b = 10

# Swapping variables

a, b = b, a

print("After swapping:")

print(a)  # Output: 10

print(b)

# Calculate area
PI = 3.14159

radius = 5

area = radius * radius
print(area)

x = 10  # Global variable


def modify_variable():
    global x

    x = 20


print("Before modification:", x)  # Output: Before modification: 10

modify_variable()

print("After modification:", x)

my_list = [1, 2, 3, 4, 5, 7, 8, 9]
print(my_list[7])
my_list.append(10)
print(my_list)
my_list.remove(3)
print(my_list)

#SET = add(1 ta just addable), remove/discard, update(onkgulo updatable) (third bracket)
#SET = Union(2 way), intersection, difference
#SUB SET, SUPER SET, DISJOINT, FROZEN SET
#symmetric difference (commongulo bad)
# convert list to tuple, list to set, tuple to set, list to set



a = {11, 12, 13, 14, 15}
a.update([20, 21])
print(a)

a.remove(12)
print(a)

a.remove(13)
print(a)

a = {11, 12, 13, 16, 17}
b = {13, 14, 15, 16, 17}


union_set = a | b
print(union_set)

intersection_set = a & b
print(intersection_set)


difference_a_b = a - b
print(difference_a_b)


squares = [x**2 for x in range(1,6)]
print(squares)

even_squares = [x**2 for x in range(1, 6) if x % 2 ==0]
print(even_squares)

a = {1,2,3,4,5,6,7,8,9}
b = list(a)
print(b, type(b))
print(tuple(a))
print(a, type(a))

x = 10  # Global variable


def modify_variable():
    global x

    x = 20


print("Before modification:", x)  # Output: Before modification: 10

modify_variable()

print("After modification:", x)

print(PI)

a = 'akil'
def brothers():
    a = 'waqil'
    return(a)
brothers()
print(a)

w = 'bilai'
def tom&jerry():
    GLOBAL_w
    w = 'idur'
    print(w)
tom&jerry()
print(w)





















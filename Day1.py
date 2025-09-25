from operator import truediv

x="pithon"
print(x,type(x))
y=23
print(y,type(y))
z=True
print(z, type(z))
A=5
B=10
A ,B = B , A
print(A,B)

a= 22
print(a, type(a))
a='twelve'
print(a, type(a))
a=True
print(a, type(a))

r = 4
area = 3.1416*r*r
print(area)

a=12
b=10
c=20
d=a+b+c
print(d,type(d))

length=12
width=20
result=0.5*12*20
print(result)


# Area of square
a=40
area_of_square= a*a
print(area_of_square)

length=43
width=87
result=length*width
print(result)

s = "hello Pyhton"

s = "12.666"
print(s, type(s))

# the python is a good programming language

"""the
python is
a good programming
language """


s= "hello python"

print(s[3:9])

student={
    'Name':'Fahim',
    'age':21,
    'Grades':[41,52,33]
    }
print(student)
student['age']=33
print(student)
print(student['age'])

x=22
y=75
z=(x*y)
print(z)
w=2*(x+y)
print(w)


print(student['Name'])
student['Grades'].append(95)
print(student['Grades'])

average_grade=sum(student["Grades"])
print(average_grade)

student["Grades"].remove(41)
print(student["Grades"])

student['major']= "mathematics"
print (student['major'])
print(student)

#1
pie=3.1416
r=4
area_of_circle=pie*r*r
print(area_of_circle, type(area_of_circle))

#2
x=74
y=56
multiplication=x*y
print(multiplication)
sum=x+y
print(sum)

#3
w=40
x=74
y=80
Area_of_trapezoid=((x+y)/2)*w
print(Area_of_trapezoid)

#integer
a=5
print(type(a))

#float
b=3.14
print(type(b))

#complex
c=3+2j
print(type(c))

s='Hello World!'
print(s[-4])

print(s[7:-12])
print(s.lower()) #???????

x=True
y=False
print(x and y) #first capitalization is mandatory

print (x or y)
print(not x)

my_list = [1,2,3,4,5,6,7,8]
print(my_list[-5])
my_list.append(6)
print(my_list)
my_list.remove(3)
print(my_list) #difference between tuple and list

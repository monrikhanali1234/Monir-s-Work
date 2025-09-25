

for x in range(10):
    print("hello world")

for i in range(90,100,5):
    print(i)

total = 0
for i in range(1,10):
    total = total + i

print(total)

for i in range(1, 21):
    if i % 5 == 0:
        print(i)

total = 0
for i in range(1,10):
    total = total + i

n = int(input('Enter value:'))

total = 0
for i in range(1, n+1):
    total += i

print(f'Sum of the first {n} natural number is {total}')

word = input("Enter a word: ")
reversed_word = ""
for letter in word:
 reversed_word = letter + reversed_word
print(f"Reversed word: {reversed_word}")

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

numbers = [10, 20, 4, 45, 99]
largest = numbers[0]
for num in numbers:
 if num > largest:
  largest = num
print(f"The largest number is {largest}")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
     print("*", end="")
print()


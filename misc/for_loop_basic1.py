# 1. Basic
from audioop import mul


for i in range(151):
    print(i)

# 2. Multiples of Five
for i in range(5, 1001, 5):
    print(i)

# 3. Counting, the Dojo Way 
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge
sum = 0
for i in range(1, 500000, 2):
    sum += i
print(sum)

# 5. Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# 6.Flexible Counter
lowNum = 0
highNum = 100
mult = 25
for i in range(lowNum, highNum + 1, mult):
    if i % mult == 0:
        print(i)

num1 = 42 # variable declaration # Data Types - Primitive - Numbers
num2 = 2.3 # variable declaration # Data Types - Primitive - Numbers
boolean = True # variable declaration # Data Types - Primitive - Boolean
string = 'Hello World' # variable declaration # Data Types - Primitive - Numbers
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration # Data Types - Composite - List - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration # Data Types - Composite - Dictionary - initialize
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration # Data Types - Composite - Tuples - initialize
print(type(fruit)) # log statement # type check
print(pizza_toppings[1]) # log statement # Data Types - Composite - List - access value
pizza_toppings.append('Mushrooms') # Data Types - Composite - List - add value
print(person['name']) # log statement # Data Types - Composite - Dictionary - access value
person['name'] = 'George' # Data Types - Composite - Dictionary - add value
person['eye_color'] = 'blue' # Data Types - Composite - Dictionary - add value
print(fruit[2]) # log statement # Data Types - Composite - Tuples - access value

if num1 > 45: # conditional - if
    print("It's greater") # log statement
else: # conditional - else
    print("It's lower") # log statement

if len(string) < 5: # length check # conditional - if
    print("It's a short word!") # log statement
elif len(string) > 15: # length check # conditional - else if
    print("It's a long word!") # log statement
else: # conditional - else
    print("Just right!") # log statement

for x in range(5): # for loop - start
    print(x) # log statement
for x in range(2,5): # for loop - start
    print(x) # log statement
for x in range(2,10,3): # for loop - start
    print(x) # log statement
x = 0 # variable declaration # Data Types - Primitive - Numbers # while loop - start
while(x < 5): # while loop - start
    print(x) # log statement
    x += 1 # while loop - increment

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) # log statement
person.pop('eye_color') # Data Types - Composite - List - delete value
print(person) # log statement

for topping in pizza_toppings: # for loop - start
    if topping == 'Pepperoni': # conditional - if
        continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional - if
        break

def print_hello_ten_times(): # function
    for num in range(10): # for loop - start
        print('Hello') # log statement

print_hello_ten_times()

def print_hello_x_times(x): # function
    for num in range(x): # for loop - start
        print('Hello') # log statement

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # function
    for num in range(x): # for loop - start
        print('Hello') # log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

# - comment - multiline
"""
Bonus section
"""

# print(num3) # comment - single line
# num3 = 72 # comment - single line
# fruit[0] = 'cranberry' # comment - single line
# print(person['favorite_team']) # comment - single line
# print(pizza_toppings[7]) # comment - single line
#   print(boolean) # comment - single line
# fruit.append('raspberry') # comment - single line
# fruit.pop(1) # comment - single line
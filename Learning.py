# This Is A Comment

from tokenize import maybe


print("Hello World!")
print('Lucas')

meal = "An english muffin"
meal = "Pasta"
meal = "Steak"
print(meal)

release_year = 5
runtime = 2
rating_out_of_10 = 9.8

print(25 * 68 + 13 / 28)

quilt_width = 8
quilt_length = 12
quilt_length = 8
print(quilt_width * quilt_length)

print(4 ** 2)
print(7 ** 2)
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 * 6 * 6 ** 2)

age = 16
text1 = 'i am'
text2 = 'years old'
my_age = text1 + ' ' + str(age) + ' ' + text2
print(my_age)

# Concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

# Prints the message
print(message)

# Plus Equals
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00

# Update total_price here:
total_price += nice_sweater
total_price += fun_books

print("The total price is", total_price)

# Multi Line String
# Assign the string here
to_you = '''Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?'''
print(to_you)

# Review
my_age = 16
half_my_age = my_age / 2
greeting = 'おはよう'
name = 'Lucas'
greeting_with_name = greeting + ' ' + name + '!'
print(greeting_with_name)

# Input
#input('do you like sushi? ')


# Boolean
set_to_true = True
set_to_false = False

bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

print(bool_one)    # True
print(bool_two)    # False
print(bool_three)  # True

my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))

# If Statements

if 2 == 4 - 2:
    print("apple")

is_raining = True
if is_raining:
    print('Bring and umbrella!')

# Relational Operators 2

x = 20
y = 20

# Write the first if statement here:
if x == y:
    print("These numbers are the same")

credits = 120

# Write the second if statement here:
if credits >= 120:
    print("You have enough credits to graduate!")

# And Statements

(1 + 1 == 2) and (2 + 2 == 4)   # True

(1 > 9) and (5 != 6)            # False

(1 + 1 == 2) and (2 < 1)        # False

(0 == 10) and (1 + 1 == 1)      # False

# More And Statements

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
    print("You meet the requirements to graduate!")

    True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")

# Else Statements
age = 12

if age >= 13:
    print("Access granted.")
else:
    print("Sorry, you must be 13 or older to watch this movie.")

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")

# Elif Statements

donation = 1500

print("Thank you for the donation!")

if donation >= 1000:
    print("You've achieved platinum status")
elif donation >= 500:
    print("You've achieved gold donor status")
elif donation >= 100:
    print("You've achieved silver donor status")
else:
    print("You've achieved bronze donor status")

# More Elif Practice
grade = 86

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Optional Review
# Little Codey is an interplanetary space boxer, who is trying to win
# championship belts for various weight categories on other planets
# within the solar system.
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
else:
    weight = weight * 1.19

if planet == 1:
    planet = "Venus"
elif planet == 2:
    planet = "Mars"
elif planet == 3:
    planet = "Jupiter"
elif planet == 4:
    planet = "Saturn"
elif planet == 5:
    planet = "Uranus"
else:
    planet = "Neptune"

print("You are going to " + planet + ", which has a weight of " + str(weight))

# Sal's Shipping

# Weight
weight = 2

# Ground Shipping
ground_price = 20
if weight <= 2:
  ground_price = (weight * 1.5) + 20
elif weight <= 6:
  ground_price = (weight * 3) + 20
elif weight <= 10:
  ground_price = (weight * 4) + 20
else:
  ground_price = (weight * 4.75) + 20

# Ground Shipping Premium
ground_premium_price = 125

# Drone Shipping
if weight <= 2:
  drone_price = weight * 4.5
elif weight <= 6:
  drone_price = weight * 9
elif weight <= 10:
  drone_price = weight * 12
else:
  drone_price = weight * 14.25

# Compare to see which is the cheapest shipping solution
print("Drone:", drone_price)
print("Ground:", ground_price)
print("Ground Premium:", ground_premium_price)

# Lists

heights = [61, 70, 67, 64, 65]

#broken_heights = [65 71 59 62]

ints_and_strings = [1, 2, 3, "four", "five", "ints_and_strings"]

sam_height_and_testscore = ["Sam", 67, 85.5, True]

#empty lists can be used if you plan to fill it up later
my_empty_list = []

example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)

orders = ["daisies", "periwinkle"]

print(orders)

orders.append("tulips")
orders.append("roses")
print(orders)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders

print(new_orders)

#broken_prices = [5, 3, 4, 5, 4] + 4

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]
print(employees[5])

#Negative indexing

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]

print(last_element, index5_element)

garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[0] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# Your code below: 
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
#new_store_order_list.remove("Onions")

#A 2d list with three lists in each of the indices. 
tic_tac_toe = [
            ["X","O","X"], 
            ["O","X","O"], 
            ["O","O","X"]
]
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
ages = [["Aaron", 15], ["Dhruti", 16]]

#2D Lists (Nested Arrays)
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)

#Editing 2D Lists
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)

#Practice
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[2][-1] = False
print(customer_data)
customer_data[1].remove(False)
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

# Python List Methods
# .count - a list method to count the current number of occurrences of an element in a list.
# .insert - a list method to insert an element into a specific index of a list.
# .pop - a list method to remove an element from a specific index or from the end of a list.
# range() - A built-in Python function to create a sequence of integers.
# len() - A built-in Python function to get the length of a list.
# .sort() / sorted() - A method and a built-in function to sort a list.

# Adding by index: Insert
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)

# Removing by index: Pop
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)
data_science_topics.pop(-2)
print(data_science_topics)

# Consecutive Lists: Range
my_range = range(10)
my_range_listed = list(my_range)
print(my_range)
print(my_range_listed)
# Your code below: 

number_list = range(9)
print(list(number_list))
zero_to_seven = range(8)
print(list(zero_to_seven))

# The Power Of Range!
range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)

# Length
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)
big_range_length = len(big_range)
print(big_range_length)

# Slicing Lists 1
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
middle = suitcase[2:4]

# Your code below: 
print(beginning)

# Slicing Lists 2
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# Counting in a list
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)

# Sortin Lists 1
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

# Sorting Lists 2
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)

# Review
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory.sort()
print(inventory)

print('''
''')
# Tuple Practice
my_info = ('Lucas', '16', 'Student')
name, age, occupation = my_info
print(my_info[-1])
print(name)
# Produces Error:
# my_info[0] = 'Lart'
# one element tuples will return what inside the parenthases because parenthases are used in order of operations in math
# For example:
mathOperation = (5+3) * 3
print(mathOperation)
one_element_tuple = (4)
print(one_element_tuple)
# As soon as it has the comma is when it becomes a tuple
example_tuple = (4,)
print(example_tuple)

print('''
''')

# Using The Zip Function
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
names_and_dogs_names = zip(owners, dogs_names)
print(names_and_dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

### LOOPS ###

# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")

# For Loops Introduction
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)

# For loops using range
promise = "I will finish the python loops module!"

for promises in range(5):
  print(promise)

# While Loops Introduction
# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")

# Your code below: 
countdown = 10
while countdown >=0:
  print("We have liftoff!")
  countdown -= 1

countdown = 10  
while countdown >= 0:
    print(countdown)
    countdown -= 1

countdown = 100
while countdown >=0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

'''# Personal Test (Infinite Loop)
count = 0
while count == 0:
    print("hi")
'''

# While Loop Lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

#Your code below: 
while index < length:
  print("I am learning about " + str(python_topics[index]))
  index += 1

# Infinite loops  
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
'''
for student in students_period_A:
  students_period_B.append(student)
  print(student)
print(students_period_B)
'''

# Loop Control: Break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# Loop Control: Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for legal_age in ages:
  if legal_age < 21:
    continue
  print(legal_age)

# Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
  print(location)
  for scoops in location:
    scoops_sold += scoops
print(scoops_sold)

print('''
End Of Code''')
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

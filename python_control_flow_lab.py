# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

vowels = 'aeiou'
letter = input('Please enter a letter from the alphabet (a-z or A-Z):').lower()

if letter in vowels:
  print(f'The letter {letter} is a vowel')
else:
  print(f'The letter {letter} is a consonant')



# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ''
while phrase != 'quit':
  phrase = input('Please enter a word or phrase:')
  print(f'What you entered is {len(phrase)} characters long')



# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

human_years = float(input('Input a dog\'s age:'))
if human_years <= 0:
  dog_years = 0
elif human_years <= 2:
  dog_years = human_years*10
else:
  dog_years = 20 + 7*(human_years - 2)
print(f'The dog\'s age in dog years is {dog_years}')



# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Please input the lengths of three sides of a triangle:')
side_a = input('Side a: ')
side_b = input('Side b: ')
side_c = input('Side c: ')

#Edge case: user inputs a negative number
sides = [float(side_a), float(side_b), float(side_c)]
if any(side < 0 for side in sides):
  output = "No negative side lengths allowed. Please try again."
else:
  output = "A triangle with sides of side_a, side_b, & side_c is a type_of_triangle triangle"

#Side comparison logic - determine type of triangle
if side_a == side_b and side_b == side_c:
  type_of_triangle = 'n equilateral'
elif side_a == side_b or side_b == side_c or side_a == side_c: 
  type_of_triangle = 'n isosceles'
else:
  type_of_triangle = ' scalene'

#Output
print(output.replace("side_a", side_a).replace("side_b", side_b).replace("side_c", side_c).replace(" type_of_triangle", type_of_triangle))



# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

fibonacci_sequence = {}
for i in range(0, 50, 1):
  if i == 0:
    fibonacci_sequence[i] = 0
  elif i == 1:
    fibonacci_sequence[i] = 1
  else:
    fibonacci_sequence[i] = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
  print(fibonacci_sequence[i])



# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
month_input = input('Enter the month of the year (Jan - Dec): ').lower()
while month_input not in months:
  print('Invalid input. Please enter the month three-letter abbreviation')
  month_input = input('Enter the month of the year (Jan - Dec): ').lower()
month_num = months.index(month_input)

days = range(1, 32, 1)
day_input = int(input('Enter the day of the month (1-31): '))
while day_input not in days:
  print('Invalid input. Please enter the day of the month (1-31): ')
  day_input = int(input('Enter the day of the month (Jan - Dec):'))

date_num = month_num*30 + day_input
print(date_num)

if date_num < 80:
  season = 'winter'
elif date_num < 171:
  season = 'spring'
elif date_num < 262:
  season = 'summer'
elif date_num < 351:
  season = 'fall'
else:
  season = 'winter'

output = 'month day is in season'
print(output.replace('month', month_input).replace('day', str(day_input)).replace('season', season))



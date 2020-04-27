# You started a new Fintech study group recently.
# You meet 4 times a month of which 3 times go online and 1 offline.
# Code a program that determines meeting dates offline under conditions as below:

# Condition 1: Pick a random date
# Condition 2: the date shall be within 28th day considering different days in each month
# Condition 3: Exclude the first 3 days in a month for preparing study

# Print a text "Our offline date is determined to be on Xth every months"

from random import *
offline_date = randint(4, 28)
print("Our offline date is determined to be on",offline_date,"th every month")
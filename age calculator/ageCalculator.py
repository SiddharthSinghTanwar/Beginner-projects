# Instead of Band Name Generator, I made a simple program that asks for you name and the year you were born and then tells you how old you are.

import datetime
name = input("What is your name?")
born_year, born_month, born_day = input("When were you born? yyyy/mm/dd:").split('/')
born_year = int(born_year)
born_month = int(born_month)
born_day = int(born_day)
today = datetime.date.today()

age = today.year - born_year - ((today.month, today.day) < (born_month, born_day)) # This is a cool way to calculate age. It is a tuple comparison. 
# It works because the tuple is compared lexicographically. So, if the month is less than the born month, then the age is reduced by 1. 
# If the month is the same, then the day is compared. If the day is less than the born day, then the age is reduced by 1. 
# If the day is greater than the born day, then the age is not reduced. If the day is the same, then the age is not reduced.
# The value 1 represents True and 0 represents False. A comparison returns a boolean value. So, if the comparison is True, then the age is reduced by 1.
print(age)
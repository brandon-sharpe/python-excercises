# #1 Conditional Basics
   #1.A)prompt the user for a day of the week, 
    # print out whether the day is Monday or not
is_it_monday = input(f"# 1.A) What day of the week is it? ")
if is_it_monday.lower() == "monday":
    print("   Damn today is Monday!")
else:
    print("    Today is not Monday!")

##1.B) prompt the user for a day of the week,
# print out whether the day is a weekday or a weekend
is_it_the_weekend = input(f"# 1.B) What day of the week is it? ")
if is_it_the_weekend.lower() == "saturday":
    print("    IT'S THE WEEKEND!")
elif is_it_the_weekend.lower() == "sunday":
    print("    IT'S THE WEEKEND!")


else:
    print("   Damn today is a weekday!")
# # 1.C) create variables and make up values for
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

hours_per_week= 60
hourly_rate =45

if hours_per_week > 40:
    print(f"You made ${(hours_per_week - 40)* hourly_rate*1.5 + 40*hourly_rate} for working {hours_per_week} hours this week, at the rate of ${hourly_rate} an hour")
else:
    print(hours_per_week*hourly_rate)

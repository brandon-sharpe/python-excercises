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
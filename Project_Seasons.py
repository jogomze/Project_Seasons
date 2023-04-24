# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

# The dates for each season in the northern hemisphere are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19
# Get input
month = input("Enter month: ")
day = int(input("Enter day: "))

# check if the input month and day are valid
valid_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
valid_days = {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

if month not in valid_months:
    print("Invalid month input")
elif day < 1 or day > valid_days[month]:
    print("Invalid day input")
else:
    # determine the season based on the dates for each season in the northern hemisphere
    if (month == "December" and day >= 21) or (month == "March" and day < 20) or month in ["January", "February"]:
        print("Winter")
    elif (month == "March" and day >= 20) or (month == "June" and day < 21) or month == "April":
        print("Spring")
    elif (month == "June" and day >= 21) or (month == "September" and day < 22) or month == "July":
        print("Summer")
    else:
        print("Autumn")
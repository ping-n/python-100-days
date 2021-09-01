year = int(input("Which year do you want to check? "))

print(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is a not leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

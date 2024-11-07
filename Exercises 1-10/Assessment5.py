print("\n----------EXERCISE 5---------\n")

months = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
        11: 30,
        12: 31}
month_number = int(input("Enter Month Number:  "))
if 1 <= month_number <= 12:
    if month_number == 2:
        feb = int(input("Input the year:  "))
        if (feb % 4 == 0) or (feb % 400 == 0):
            print("This year has 29 days.")
        else:
            print("This year has 28 days.")
    else:       
        print(f"This month has {months[month_number]} days!")
else: 
    print("The number of the month does not exist.")
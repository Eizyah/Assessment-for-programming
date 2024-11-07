print("\n----------EXERCISE 6---------\n")

Attempt = 5
remaining = 0
Correctpin = 12345
while remaining < Attempt:
    pin = int(input("Enter Pin:  "))
    if pin == Correctpin: 
        print("Correct Pin!")
        break
    else: 
        remaining += 1
        remaining_attempts = Attempt - remaining
        if remaining_attempts > 0:
            print(f"Incorrect password. Remaining attempts: {remaining_attempts}")
else:
    print("Maximum attempts reached. Authorities have been alerted")
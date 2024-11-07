print("\n----------EXERCISE 10---------\n")

def odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Input a number: "))
answer = odd_or_even(number)
print(answer)

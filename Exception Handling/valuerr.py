try:
    x = int(input("Enter a number: "))
    print(f"You entered {x}")
except ValueError:
    print("That was not a valid number!")

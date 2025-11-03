try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Number must be positive.")
except ValueError as e:
    print("Error:", e)
else:
    print(f"Good job! You entered {num}.")
finally:
    print("Program finished.")

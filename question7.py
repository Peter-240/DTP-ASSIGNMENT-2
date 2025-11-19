age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    print("Valid age:", age)
else:
    print("Invalid input, must be a number.")

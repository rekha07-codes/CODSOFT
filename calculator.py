print("=== My Calculator ===")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    result = first_number + second_number
    print("Result =", result)

elif choice == "2":
    result = first_number - second_number
    print("Result =", result)

elif choice == "3":
    result = first_number * second_number
    print("Result =", result)

elif choice == "4":
    if second_number != 0:
        result = first_number / second_number
        print("Result =", result)
    else:
        print("Error! Division by zero is not allowed.")

else:
    print("Invalid choice! Please select a number from 1 to 4.")

print("Thank you for using my calculator!")
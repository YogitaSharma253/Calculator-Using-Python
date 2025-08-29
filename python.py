# Calculator Project in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    print("===== Simple Calculator =====")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("0. Exit")

    while True:
        choice = input("\nEnter choice (0-6): ")

        if choice == '0':
            print("Exiting... Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"✅ Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"✅ Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"✅ Result: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"✅ Result: {num1} / {num2} = {divide(num1, num2)}")

            elif choice == '5':
                print(f"✅ Result: {num1} ^ {num2} = {power(num1, num2)}")

            elif choice == '6':
                print(f"✅ Result: {num1} % {num2} = {modulus(num1, num2)}")
        else:
            print("❌ Invalid choice! Please enter a number from 0-6.")

if __name__ == "__main__":
    calculator()
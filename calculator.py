def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! 0 se divide nahi hota"
    return x / y

print("🧮 Simple Calculator 🧮")
print("Operations: +  -  *  /")

while True:
    try:
        num1 = float(input("Pehla number daal: "))
        op = input("Operation chuno (+, -, *, /): ")
        num2 = float(input("Dusra number daal: "))

        if op == '+':
            print(f"Result: {add(num1, num2)}")
        elif op == '-':
            print(f"Result: {subtract(num1, num2)}")
        elif op == '*':
            print(f"Result: {multiply(num1, num2)}")
        elif op == '/':
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Galat operation! +, -, *, / mein se chuno")

        again = input("Phir se calculate kare? y/n: ")
        if again.lower() != 'y':
            print("Calculator band. Bye!")
            break
            
    except ValueError:
        print("Bhai number daal, text nahi!")

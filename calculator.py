def get_numbers():
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    return num1, num2

def calculator(num1,num2,op):
    if op=='+':
        return num1 + num2
    elif op=='-':
        return num1 - num2
    elif op=='*':
        return num1 * num2
    elif op=='/':
        return num1 / num2
    else:
        return "Invalid operator"
def main():
    num1, num2 = get_numbers()
    op = input("Enter operator (+, -, *, /): ").strip()
    result = calculator(num1, num2, op)
    print("Result:", result)

if __name__ == "__main__":
    main()
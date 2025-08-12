def Multiply():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    sum = num1 * num2 
    print(f"multiplied number is {sum}")
    for i in range(0,sum,num2):
        print(i)
Multiply()

import math
def check():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a second number: "))
    sum = num1 * num2 
    print(f"multiplied number is {sum}")
    for i in range(0,sum,num2):
        print(i)
    if sum <= 1:
        print("number is not an prime number")
    for i in range(1,sum,2):
        print(i)
    if sum > 1:
        print("number is a prime number")
    for a in range(1,sum,1):
        print(a)
    if sum %2 == 0:
        print("number is even")
    else:
        print("number is not an even number")
    for s in range(0,sum,2):
        print(s)
    if sum %2 != 0:
        print("number is odd")
    else:
        print("number is not an odd number")
    for d in range(1,sum,2):
        print(d)
check()
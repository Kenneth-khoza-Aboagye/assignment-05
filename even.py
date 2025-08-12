import math
def even(num):
    num1 = int(input("Enter a number: "))
    if num1 %2 != 0:
        print("number is not an even number")
        return False
    for i in range(1,num1,2):
        print(i)
    if num1 %2 == 0:
        print("number is even")
        return False
    return True 
even(sum)
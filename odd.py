import math
def if_odd(num):
    num1 = int(input("Enter an odd number: "))
    if num1 %2 != 0:
        print("number is not an odd number")
        return False
    for i in range(1,num1,2):
        print(i)
    if num1 %2 == 0:
        print("number is odd")
        return False
    return True 
if_odd(sum)

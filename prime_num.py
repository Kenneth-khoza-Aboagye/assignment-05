import math
def prime_num(num):
    num1 = int(input("Enter a number: "))
    if num1 <= 1:
        print("number is not an prime number")
        return False
    for i in range(1,num1,2):
        print(i)
    if num1 >= 1:
        print("number is a prime number")
        return False
    return True 
prime_num(sum)
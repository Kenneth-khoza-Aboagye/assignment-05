def if_odd():
    num1 = int(input("Enter an odd number: "))
    if num1 %2 != 0:
        print("number is odd")
    for i in range(1,num1,2):
        print(i)
if_odd()

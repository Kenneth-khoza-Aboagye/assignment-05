def if_even():
    num1 = int(input("Enter an even number: "))
    if num1 %2 == 0:
        print("number is even")
    for i in range(0,num1,2):
        print(i)
if_even()
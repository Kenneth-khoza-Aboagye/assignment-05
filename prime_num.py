def prime_num():
    num1 = int(input("Enter a number: "))
    if num1 %1 == 0:
        print("its a prime number")
    for i in range(1,num1):
        print(i)
prime_num()
def prime_factor(num):
    i = 2
    while num > 1:
        if(num % i == 0):
            print(i, end=" ")
            num = num // i
        else:
            i = i + 1
num = int(input("Enter any number: "))
prime_factor(num)
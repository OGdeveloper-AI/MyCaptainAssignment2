def fibonacci_number(n):
    if n <=1:
        return n
    else:
        return(fibonacci_number(n-1) + fibonacci_number(n-2))


number = int(input("Type in required numbers: "))

if number <= 0:
    print("Please type in a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(number):
        print(fibonacci_number(i))

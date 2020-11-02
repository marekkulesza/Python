#Fibonacci.py


def fib(stopHere):

    a = 0
    b = 1

    print("0")
    print("1")

    while True:
        
        x = a + b
        print(x)
        b = a
        a = x

        if x > stopHere:
            break

fib(1000)


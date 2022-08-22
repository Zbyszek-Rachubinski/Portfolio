import time

def fib_val(num):
        fibo = []

        def fibonacci(num):

                if num==0:
                        return 0
                elif num==1:
                        return 1
                else:
                        return fibonacci(num-1) + fibonacci(num-2)

        for n in range (num+1):
                fibo.append(fibonacci(n))

        number = fibo[num]

        print(number)

num = int(input("Provide a Fibonacci element number to know its value: "))

time.sleep(0.5)

print("The value of element number " + str(num) + " is: ")
fib_val(num)

time.sleep(0.5)

answer = input("Do you want to calculate another value? Press 'y' for yes, 'n' to quit. ")

while True:
    if answer == 'y':

        num = int(input("Please provide next element to calculate its value. "))

        time.sleep(0.5)
        
        print("The value of element number " + str(num) + " is: ")
        fib_val(num)

        time.sleep(0.5)
        
        answer = input("Do you want to calculate another value? Press 'y' for yes, 'n' to quit. ")

    elif answer == 'n':
        break

    else:
        answer = input("Press 'y' for yes, 'n' to quit. ")

        time.sleep(0.5)
        
quit()


import time

def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

x = int(input("Please provide a number to calculate its factorial. "))     
print("The factorial of " + str(x) + " is " + str(fact(x)) + ".")

time.sleep(0.5)

answer = input("Do you want to calculate another factorial? Press 'y' for yes, 'n' to quit. ")

while True:
    if answer == 'y':

        x = int(input("Please provide the next number to calculate its factorial. "))

        time.sleep(0.5)
        
        print("The factorial of " + str(x) + " is " + str(fact(x)) + ".")

        time.sleep(0.5)
        
        answer = input("Do you want to calculate another factorial? Press 'y' for yes, 'n' to quit. ")

    elif answer == 'n':
        break

    else:
        answer = input("Press 'y' for yes, 'n' to quit. ")

        time.sleep(0.5)
        
quit()
    

check_prime = []

number_of_nums = int(input("How many numbers do you want to check?"))

check_prime.append(int(input("Specify the first number, please.")))

for num in range(number_of_nums - 2):
    
    check_prime.append(int(input("Specify the next number, please.")))

check_prime.append(int(input("Specify the last number, please.")))

for n in check_prime:

    number = n
    factor_list = []

    for i in range (number+1):
    
        if number % (i+1) == 0:
    
            factor_list.append(i+1)
            
    if len(factor_list) > 2:
    
        print("{} is NOT a prime number, because {} is a factor of {}".format(number, factor_list[1], number))

    else:
    
        print("{} is a prime number".format(number))

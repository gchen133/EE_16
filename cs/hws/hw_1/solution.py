import math
#read string and convert each value of each character to an integer
#multiply the value with the base and its corresponding power in relation to its place in the string
#continuously add the values up until there are none left
def base_q_to_decimal(s,q):
    x = 0
    for i in range(len(s)):
        holdValue = int(s[i])
        value = holdValue*pow(q, len(s)-1-i)
        x += value
    return x
#read and create value using the same method as base_q_to_decimal
#to create the string of integers first mod the value by the new base and convert it to an int and then a char/str and add it to the string
#the devide the new value by p and repeat til the value is 0
def base_q_to_p(s,q,p):
    x = ""
    valueDec = 0
    for i in range(len(s)):
        holdValue = int(s[i])
        value = holdValue*pow(q, len(s)-1-i)
        valueDec += value
    while (valueDec > 0):
        x = str(int(valueDec % p)) + x
        valueDec = int(valueDec / p) 
    if(x == ""):
        x = "0"

    return x
#add the lists together to create one list
#using a double for loop go through each part of the list and switch any values that come before but are larger than subsequent values
#the double for loop makes sure that even if the smallest number in the list is at the end at the beginning of the code it will rise to the top
#this is the most inefficient code but is the simpliest to think and code
def sorted_merge(l1,l2):
    l = l1 + l2
    for i in range(1, len(l)):
        for j in range(1, len(l)):
            if(l[j-1] > l[j]):
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp
        
    return l
#using a for loop we can add all the values of the list of lists into a single list
#then repeating the method in sorted_merge we can order the list with a double for loop interating through each value stored in the list
def multiple_sorted_merge(l_multiple):
    l_sorted = []
    for i in range(len(l_multiple)):
        l_sorted += l_multiple[i]
    for i in range(1, len(l_sorted)):
            for j in range(1, len(l_sorted)):
                if(l_sorted[j-1] > l_sorted[j]):
                    temp = l_sorted[j]
                    l_sorted[j] = l_sorted[j-1]
                    l_sorted[j-1] = temp

    return l_sorted
#first set root and power to 0
#then in a double for loop check every value in the range of 1-6 fir the power and 1-sqrt(x) you only need to check up to square root x because you are checking for powers
#if the power and root match the integer the root and pwr varibales will change to those values
#the if loop also allows the highest power to be stored in the variables
def find_root(x):
    root = 0
    pwr = 0
    for i in range(1,6):
        for j in range(int(math.sqrt(x))+1):
            if (pow(j, i) == x):
                root = j
                pwr = i
    if (root == 0 and pwr == 0):
        return False
    return root, pwr
#first make a list of factors with the factorization function
#the list can then be compared with the other lists of factors of the other values in a for loop
#if the count of a certain factor is less than what is found in the array that value will be added to the factor list
#by multiplying the values of the resulting list we can find the least common multiple
def least_common_multiple(*args):
    factors = factorization(args[0])
    lcm = 1
    for i in range(1, len(args)):
        prime_list = factorization(args[i])
        for j in range(len(prime_list)):
            if (factors.count(prime_list[j]) < prime_list.count(prime_list[j])):
                factors += (prime_list.count(prime_list[j])-factors.count(prime_list[j])) *[prime_list[j]]
    for k in range(len(factors)):
        lcm *= factors[k]
    return lcm
#helper factorization fucntion that helps factor a value
#by first dividing by 2 until we can no longer it reduces the amount of values we have to check
#the for loop checks all odd numbers less than the input
#the while loop within it checks for repeating factors
#this creates a prime factored list
def factorization (x):
    prime_list = []
    while (x % 2 == 0):
        prime_list += [2]
        x /= 2
    for i in range(3,int(x)+1,2):
        while (x % i == 0):
            prime_list += [i]
            x /= i
    return prime_list
#Find the greatest common divisor of multiple values with the Euclidean Algorithim
#we can find the gcd of two numbers by modding the values and getting the remainder and modding again
#we do this multiple times each time we set the gcd of the previous pair to one of the values of the current pair
#When there is no more remainder the gcd will be found as the values will be the same
def greatest_common_divisor(*args):
    a = args[0]
    if (len(args) < 2):
        return a
    b = args[1]
    r = a % b
    while (r):
        a = b
        b = r
        r = a % b
    i = 2
    while (i < len(args)):
        a = args[i]
        r = a % b
        while (r):
            a = b
            b = r
            r = a % b
        i +=1
    return b
#by inputting the values from the list of lists into a set it will automatically get rid of any repeating values
#after inputting everything we can then change the set to a list creating a unique list
def unique_values(L):
    unique_list = {}
    unique_list = set()
    for i in range(len(L)):
            unique_list.update(L[i])
    list(unique_list)
    return unique_list


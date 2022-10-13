"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import os

def primes(number_of_primes):
    list = []
    num = 2
    while len(list) != number_of_primes:
        successfulDivisions = 0
        for i in range(1, num+1):
            if (num%i) == 0:
                successfulDivisions += 1
        if successfulDivisions == 2:
            list.append(num)
        num += 1
    return list

noError = False
while noError == False:
    try:
        howManyPrimes = int(input("How many prime numbers would you like to view: "))
        if howManyPrimes < 1:
            raise Exception
        print(primes(howManyPrimes))
        noError = True
    except:
        if (os.name == "nt"):
            os.system("cls")
        else:
            os.system("clear")
        print("An error occured. Please note you can only enter a whole number greater than 0.")
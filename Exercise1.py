##
# CPSC 217 Exercise 1: Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

name = input("Enter your name: ")
age = -1
while age < 0:
    try:
        age = float(input("Enter your age: "))
    except ValueError:
        # Ask user for age if input was not a number
        pass
# Display result
print("Holy moly, %s is %.1f years old! That's %.1f in dog years!" % (name, age, age*7))

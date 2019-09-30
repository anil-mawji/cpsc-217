##
# CPSC 217 Exercise 1: Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

name = input("Enter your name: ")
while True:
    try:
        age = float(input("Enter your age: "))
        if age < 0:
            # Ask user for age again
            continue
        # Display result
        print("Holy moly, %s is %.1f years old! That's %.1f in dog years!" % (name, age, age*7))
        break
    except ValueError:
        # Ask user for age if input was not a number
        pass

##
# CPSC 217 Exercise 1: Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji

name = input("Enter your name:\n")
while True:
    try:
        age = float(input("Enter your age:\n"))
        if age < 0:
            # Ask user for age again
            continue
        # Display result
        print("Holy moly,", name, "is", age, "years old! That's", age*7, "years old in dog years!")
        break
    except ValueError:
        pass

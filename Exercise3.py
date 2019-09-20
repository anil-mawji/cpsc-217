##
# CPSC 217 Exercise 3: Better Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji

while True:
    try:
        age = float(input("Enter your age:\n"))
        dogAge = 0
        # Add 10.5 years to dogAge a maximum of two times
        for i in range(0, 2):
            if age - 1 >= 0:
                dogAge = dogAge + 10.5
                age = age - 1
            else:
                # Age is too small to keep adding
                break
        # Add 4 years for every year remaining in age
        dogAge = dogAge + age*4
        if age < 0:
            # Exit program
            break
        # Display result
        print("That's equivalent to", dogAge, "dog years!")
    except ValueError:
        # If input is not a number, ask for age again
        pass

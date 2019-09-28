##
# CPSC 217 Exercise 3: Better Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji

HUMAN_TO_DOG_YEARS = 10.5


# Convert a given age to an age in dog years
# @param an age in human years
# @return an age in dog years
def get_dog_years(years):
    # First two dog years are equivalent to 10.5 human years
    return years * HUMAN_TO_DOG_YEARS if years <= 2 else (years - 2) * 4 + HUMAN_TO_DOG_YEARS * 2


while True:
    try:
        age = float(input("Enter your age: "))
        if age < 0:
            # Exit program
            break
        # Round the result to 1 decimal place
        print("That's equivalent to %.1f" % get_dog_years(age), "dog years!")
    except ValueError:
        # If input was not a number then ask for age again
        pass

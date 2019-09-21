##
# CPSC 217 Exercise 3: Better Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji


# Convert a given age to an age in dog years
# @param an age in human years
# @return an age in dog years
def get_dog_years(years):
    dog_years = 0
    if years <= 2:
        # First two dog years are equivalent to 10.5 human years
        return years * 10.5
    dog_years = 0
    # Add 10.5 years to dog_years a maximum of two times
    for i in range(2):
        if years - 1 >= 0:
            dog_years = dog_years + 10.5
            years = years - 1
        else:
            # Age is too small to keep adding
            break
    # Add 4 years for every remaining year
    return dog_years + years * 4


while True:
    try:
        age = float(input("Enter your age:\n"))
        if age < 0:
            # Exit program
            break
        # Round the result to 1 decimal place
        print("That's equivalent to", "%.1f" % get_dog_years(age), "dog years!")
    except ValueError:
        # If input was not a number then ask for age again
        pass

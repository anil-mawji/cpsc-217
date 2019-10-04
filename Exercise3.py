##
# CPSC 217 Exercise 3: Better Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809


# Convert a given age to an age in dog years
# @param an age in human years
# @return an age in dog years
def get_dog_years(years):
    # First two dog years are equal to 10.5 human years
    # Rest of dog years are equal to 4 human years
    return (years - 2) * 4 + 10.5 * 2 if years > 2 else years * 10.5


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

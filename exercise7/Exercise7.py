##
# CPSC 217 Exercise 7: Counting... 1... 2... 3...
# Name: Anil Mawji
# UCID: 30099809

with open(input("Enter the name of a file: ")) as file:
    print("That file contains", sum(len(line.split(",")) for line in file), "values.")
file.close()

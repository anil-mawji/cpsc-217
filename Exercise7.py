##
# CPSC 217 Exercise 7: Counting... 1... 2... 3...
# Copyright (C) 2019 Anil Mawji

with open(input("Enter the name of a file:\n"), "r") as f:
    print("That file contains", sum(line.count(",") for line in f), "values.")
f.close()

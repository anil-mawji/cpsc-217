##
# CPSC 217 Exercise 7: Counting... 1... 2... 3...
# Copyright (C) 2019 Anil Mawji

name = input("Enter the name of the text file:\n")
with open(name + ".txt", "r") as f:
    print(sum(line.count(",") for line in f))
f.close()

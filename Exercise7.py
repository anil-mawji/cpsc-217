##
# CPSC 217 Exercise 1: Human Years and Dog Years
# Copyright (C) 2019 Anil Mawji

name = input("Enter the name of the text file: ")
with open(name + ".txt", "r") as f:
    count = sum(line.count(",") for line in f)
f.close()

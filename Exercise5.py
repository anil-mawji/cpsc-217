##
# CPSC 217 Exercise 5: Forward and Backward
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

value, tab = "x", []
while len(value) != 0:
    value = input("Enter a value (blank line to quit): ")
    # Add value to the list
    tab.append(value)
# Display list in reverse order
print(*reversed(tab), sep="\n")

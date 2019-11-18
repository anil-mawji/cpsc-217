##
# CPSC 217 Exercise 5: Forward and Backward
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809

table, value = [], input("Enter a value (blank line to quit): ")
while value != "":
    # Add value to the list
    table.append(value)
    value = input("Enter a value (blank line to quit): ")
# Display list in reverse order
print(*reversed(table), sep="\n")

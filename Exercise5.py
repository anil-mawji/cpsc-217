##
# CPSC 217 Exercise 5: Forward and Backward
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809


value, tab = None, []
while True:
    value = input("Enter a value (blank line to quit): ")
    # If user did not enter input, break loop
    if len(value) == 0:
        break
    # Add value to the list
    tab.append(value)
# Display list in reverse order
print(*reversed(tab), sep="\n")

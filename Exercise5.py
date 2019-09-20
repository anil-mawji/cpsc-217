value, tab = None, []
while value != " ":
    if value is not None:
        tab.append(value)
    value = input("Enter a value (blank line to quit):\n")
# Display list in reverse order
print(*reversed(tab), sep="\n")

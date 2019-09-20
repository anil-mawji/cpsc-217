value, tab = None, []
while value != " ":
    if value is not None:
        tab.append(value)
    value = input("Enter a value (blank line to quit): ")
print(*reversed(tab), sep="\n")

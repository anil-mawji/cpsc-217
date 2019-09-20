value, tab = None, []
while value != " ":
    if value is not None:
        tab.append(value)
    value = input("Enter a value (blank line to quit): ")
for v in reversed(tab):
    print(v)  # print(tab[::-1])

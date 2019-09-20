name = input("Enter the name of a file: ")
with open(name, "r") as f:
    count = sum(line.count(",") for line in f)
f.close()

PROVINCE_LETTERS = {
    "T": "Alberta",
    "V": "British Columbia",
    "R": "Manitoba",
    "E": "New Brunsiwick",
    "A": "Newfoundland",
    "B": "Nova Scotia",
    "X": "Nunavut or Northwest Territories",
    "K": "Ontario",
    "L": "Ontario",
    "M": "Ontario",
    "N": "Ontario",
    "P": "Ontario",
    "C": "Prince Edward Island",
    "G": "Quebec",
    "H": "Quebec",
    "J": "Quebec",
    "S": "Saskatchewan",
    "Y": "Yukon"
}

postalCode = input("Enter a 6 character postal code (A1A1A1): ")
print("That postal code resides in", PROVINCE_LETTERS[postalCode[0]])

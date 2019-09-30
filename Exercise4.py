##
# CPSC 217 Exercise 4: The Exercise Due on the 23rd Day of the 7th Month
# Copyright (C) 2019 Anil Mawji
# UCID: 30099809


def int2ordinal(num):
    return str(num) + "th" if num % 100 == 11 or num % 100 == 12 or num % 100 == 13 else \
        str(num) + "st" if num % 10 == 1 else \
        str(num) + "nd" if num % 10 == 2 else \
        str(num) + "rd" if num % 10 == 3 else str(num) + "th"

###############################################################################
#
#  Don't change any code below this point in the file.
#
###############################################################################

# Demonstrate the int2ordinal function by reading a day, month and year and
# displaying the entered values as ordinal numbers as part of a longer message.
def main():
  day = int(input("Enter a day between 1 and 31: "))
  month = int(input("Enter a month between 1 and 12: "))
  year = int(input("Enter a year between 1 and 2100: "))

  print("On the", int2ordinal(day), "day of the", int2ordinal(month), \
        "month of the", int2ordinal(year), "year, something amazing happened!")

# Call the main function
main()

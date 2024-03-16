# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
print(string1)
string1 = string1.capitalize()
print(string1)

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
print(string2)
string2 = string2.center(10, " ")
print(string2)

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
endsInOn = string3.endswith("on")
print(endsInOn)

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
indexTH = string4.find("th")
print(indexTH)

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
alnum = string5.isalnum()
print(alnum)

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
alphabetic = string6.isalpha()
print(alphabetic)

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
allLower = string7.islower()
print(allLower)

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespace
string8 = "   "
allSpaces = string8.isspace()
print(allSpaces)

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
isUpper = string9.isupper()
print(isUpper)

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
newString = separator.join(iterable1)
print(newString)

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
lowerString10 = string10.lower()
print(lowerString10)

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  python"
lstrip = string11.lstrip()
print(lstrip)

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "python  "
rstrip = string12.rstrip()
print(rstrip)

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
replaceStr = string13.replace("python", "snake")
print(replaceStr)

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
rfind = string14.rfind("n")
print(rfind)

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
split = string15.split("-")
print(split)

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
startsWith = string16.startswith("py")
print(startsWith)

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
strip = string17.strip(" ")
print(strip)

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
swapCase = string18.swapcase()
print(swapCase)

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
title = string19.title()
print(title)

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
allUpper = string20.upper()
print(allUpper)
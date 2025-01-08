# Remember that strings are immutable which means that you can't 
# change the value of a string once it has been created.
# Original string
name  = "!!Regved  !!!"
print(name)
# Converts string to uppercase
print(name.upper())
# Converts string to lowercase
print(name.lower())
# Removes leading and trailing whitespace and specified characters
print(name.strip())
# Removes leading specified characters
print(name.lstrip("!"))
# Removes trailing specified characters
print(name.rstrip("!"))
# Replaces all occurrences of first string with second string
print(name.replace("!", "?"))
# Splits string into list based on delimiter
print(name.split(" "))

sentence = "Knull is the creator of Symbiotes"
# Converts first character to uppercase and rest to lowercase
print(sentence.capitalize())
# Returns centered string with specified width
print(sentence.center(50))
# Returns count of substring occurrences
print(sentence.count("S"))
# Checks if string starts with specified substring
print(sentence.startswith("S"))
# Checks if string ends with specified substring
print(sentence.endswith("s"))
# Checks if string ends with substring in specified range
print(sentence.endswith("the", 0, 10))
# Returns lowest index of substring (-1 if not found)
print(sentence.find("S"))
# Returns lowest index of substring (-1 if not found)
print(sentence.index("S"))
# Checks if all characters are alphanumeric A-Z, a-z, 0-9
print(sentence.isalnum())
# Checks if all characters are alphabetic A-Z, a-z
print(sentence.isalpha())
# Checks if all characters are digits 0-9
print(sentence.islower())
# Checks if all characters are whitespace
print(sentence.isprintable())
# Checks if all characters are uppercase
print(sentence.isupper())
# Checks if all characters are lowercase
print(sentence.islower())
# Checks if string starts with title case (first letter capital)
print(sentence.istitle())
# Returns string right justified with specified width
print(sentence.rjust(50))
# Returns string left justified with specified width
print(sentence.ljust(50))
# Joins iterable elements with string as separator
print("-".join(["Hello", "World"]))
# Removes specified prefix from string if present
print(sentence.removeprefix("Knull"))
# Removes specified suffix from string if present
print(sentence.removesuffix("Symbiotes"))
# Checks if string contains only whitespace
print(sentence.isspace())
# Checks if all characters are decimal (0-9)
print(sentence.isdecimal())
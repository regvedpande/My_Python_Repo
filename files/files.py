#r mode is default mode even if not specified
a = open("regved.txt", "r")
text = a.read()
print(text)
a.close()

#w mode is used to write to a file
b = open("regved.txt", "w")
b.write("Assassin Creed Shadows")
b.close()
f = open("regved.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

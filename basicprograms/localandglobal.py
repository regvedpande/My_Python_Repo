y = 10
print(y)

def access():
    global y
    y = 20
    print(y)

access()
print(y)
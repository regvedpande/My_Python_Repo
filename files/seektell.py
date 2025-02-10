with open('regved.txt', 'r') as regved:
    print(type(regved))
    
    regved.seek(10)
    
    print(regved.tell())
    data  = regved.read()
    print(data)
    

    
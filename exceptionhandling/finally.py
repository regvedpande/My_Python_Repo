def scope():
    try:
        l = [1,4,6,8]
        take = int(input("Enter a number: "))
        print(l[take])
        return 1
    except:
        print("An error occurred")
        return 0
    finally:
        print("The 'try except' is finished")

x = scope()
print(x)
  
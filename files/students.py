f = open("students.txt", "w")
i = 0
while True:
    i+=1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in subject 1 is {m1}")
    print(f"Marks of student {i} in subject 2 is {m2}")
    print(f"Marks of student {i} in subject 3 is {m3}")
    print(line)
f.close()
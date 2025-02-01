import os

if not os.path.exists("test.txt"):
    os.makedirs("test.txt")
    
for i in range(2):
    os.makedirs(f"data/Day{i+1}", exist_ok=True)
    
for i in range(2):
    os.rename(f"data/Day{i+1}", f"data/Day{i+1}_Renamed")
    
folders = os.listdir("data")

for folder in folders:
    print(folder)
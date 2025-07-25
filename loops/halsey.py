# Prime number finder in a given range
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):
    if num > 1:  # Primes are greater than 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(f"{num} is a prime number")
questions = [["Who is the father of computer science?", "Charles Babbage", "Alan Turing", "Tim Berners Lee", "Bill Gates", 1], 
["Who is the founder of Microsoft?", "Charles Babbage", "Alan Turing", "Tim Berners Lee", "Bill Gates", 4], 
["Who is the founder of World Wide Web?", "Charles Babbage", "Alan Turing", "Tim Berners Lee", "Bill Gates", 3],
["Who is the founder of Apple Inc.?", "Charles Babbage", "Steve Jobs", "Tim Berners Lee", "Bill Gates", 2]]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

money = 0
print("Welcome to KBC! Enter 0 at any time to quit the game.")
for i in range(len(questions)):
    current_question = questions[i]
    print(f"\nQuestion for Rupees {levels[i]}")
    print(current_question[0])
    print(f"1. {current_question[1]}    2. {current_question[2]}") 
    print(f"3. {current_question[3]}    4. {current_question[4]}")
    answer = input("Enter your answer (1-4) or 0 to quit: ")
    
    if answer.lower() == 'q' or answer == '0':
        confirm = input("Are you sure you want to quit? (y/n): ")
        if confirm.lower() == 'y':
            print(f"\nYou have quit the game. You take home Rs. {money}")
            break
        else:
            continue
            
    try:
        answer = int(answer)
        if answer == current_question[5]:
            money = levels[i]
            print(f"Correct answer! You have won Rs. {money}")
        else:
            print("Wrong answer!")
            break
    except ValueError:
        print("Invalid input! Please enter a number between 0-4")
        break

print(f"\nGame Over! You won Rs. {money}")


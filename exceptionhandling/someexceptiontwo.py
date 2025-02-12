try:
    with open("games.txt", "r") as f:
        games = f.readlines()
        for game in games:
            print(game.strip())
except FileNotFoundError:
    print("The file 'games.txt' was not found. Please make sure the file exists.")
except PermissionError:
    print("You do not have the necessary permissions to read 'games.txt'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

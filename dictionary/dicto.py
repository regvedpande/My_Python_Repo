import random

# Create a dictionary with random data
random_dict = {
    "name": "John Doe",
    "age": random.randint(18, 65),  # Random age between 18 and 65
    "city": random.choice(["New York", "London", "Mumbai", "Tokyo"]),  # Random city from a list
    "score": random.uniform(50, 100)  # Random score between 50 and 100
}

# Print the entire dictionary
print("Random Dictionary:", random_dict)

# Access individual values
print("\nAccessing Values:")
print("Name:", random_dict["name"])
print("Age:", random_dict["age"])
print("City:", random_dict["city"])
print("Score:", round(random_dict["score"], 2))  # Rounded for better readability

# Add a new key-value pair
random_dict["profession"] = random.choice(["Engineer", "Doctor", "Artist", "Teacher"])
print("\nAfter Adding Profession:", random_dict)

# Iterate through the dictionary
print("\nIterating Through the Dictionary:")
for key, value in random_dict.items():
    print(f"{key}: {value}")

# Check if a key exists
print("\nChecking for Key Existence:")
key_to_check = "city"
if key_to_check in random_dict:
    print(f"The key '{key_to_check}' exists with value '{random_dict[key_to_check]}'")
else:
    print(f"The key '{key_to_check}' does not exist.")

# Remove a key-value pair
removed_value = random_dict.pop("score", None)  # Safely remove 'score' if it exists
print("\nAfter Removing Score:", random_dict)
print("Removed Value:", round(removed_value, 2) if removed_value else None)
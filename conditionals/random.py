import random

def random_conditional_action():
    """
    Performs a random action based on random conditions.
    """

    # Generate random values for conditions
    random_number = random.randint(1, 100)
    random_boolean = random.choice([True, False])
    random_string = random.choice(["apple", "banana", "cherry"])

    # Conditional logic
    if random_number > 50 and random_boolean:
        print(f"Condition 1: Number > 50 and Boolean is True. Number: {random_number}")
        print("Action: Performing action A.")
        # Perform action A (e.g., call a function, modify a variable)
        result = random_number * 2
        print(f"Result of action A: {result}")

    elif random_string == "banana" or random_number % 2 == 0:
        print(f"Condition 2: String is 'banana' or Number is even. String: {random_string}, Number: {random_number}")
        print("Action: Performing action B.")
        # Perform action B
        result = random_string.upper()
        print(f"Result of action B: {result}")

    elif not random_boolean:
        print(f"Condition 3: Boolean is False. Boolean: {random_boolean}")
        print("Action: Performing action C.")
        # Perform action C
        print("Nothing to do here.")

    else:
        print("No conditions met. Performing default action.")
        # Default action
        print("Default action completed")

# Run the function multiple times to see different outcomes
for _ in range(5):
    random_conditional_action()
    print("-" * 20)  # Separator

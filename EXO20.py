# Initialize an empty list to store user input
user_list = []

# Continuously ask the user for numbers
while True:
    # Ask the user to input a number
    user_input = input("Enter a number: ").strip()
    
    # Handle non-integer inputs
    try:
        number = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Stop if the user enters 0
    if number == 0:
        break

    # Add the number to the list
    user_list.append(number)

    # Print the current list and the sorted list
    print(f"Current List: {user_list}")
    print(f"Sorted List: {sorted(user_list)}")

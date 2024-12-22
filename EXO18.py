# Initialisation de la liste
numbers = [1, 2, 3, 4, 5]

# Affichage du menu
def display_menu():
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")

# Programme principal
while True:
    # Afficher la liste actuelle
    print("\nCurrent List:", numbers)
    # Afficher le menu
    display_menu()
    
    try:
        # Demander à l'utilisateur de choisir une option
        choice = int(input("Choose an option: "))
        
        if choice == 1:  # Append
            value = int(input("Enter value to append: "))
            numbers.append(value)
            print("Updated List:", numbers)

        elif choice == 2:  # Insert
            value = int(input("Enter value to insert: "))
            index = int(input("Enter index to insert at: "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print("Updated List:", numbers)
            else:
                print("Error: Index out of range.")

        elif choice == 3:  # Pop
            if numbers:
                index = int(input("Enter index to pop (leave empty for last element): ") or -1)
                if index == -1:
                    popped_value = numbers.pop()
                elif 0 <= index < len(numbers):
                    popped_value = numbers.pop(index)
                else:
                    print("Error: Index out of range.")
                    continue
                print(f"Popped value: {popped_value}")
                print("Updated List:", numbers)
            else:
                print("Error: List is empty, nothing to pop.")

        elif choice == 4:  # Remove
            if numbers:
                value = int(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                    print("Updated List:", numbers)
                else:
                    print("Error: Value not found in list.")
            else:
                print("Error: List is empty, nothing to remove.")

        elif choice == 5:  # Quit
            print("Exiting program. Final List:", numbers)
            break

        else:
            print("Error: Invalid option. Please choose a valid number.")

    except ValueError:
        print("Error: Invalid input. Please enter a number.")

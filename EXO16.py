# Initialisation de la liste
numbers = [1, 2, 3, 4, 5]

while True:
    # Demander un index à l'utilisateur
    index = int(input("Enter index (-1 to quit): "))

    # Condition de sortie
    if index == -1:
        break

    # Vérifier si l'index est valide
    if 0 <= index < len(numbers):
        # Demander une nouvelle valeur
        new_value = int(input("Enter new value: "))
        # Mettre à jour la liste
        numbers[index] = new_value
        # Afficher la liste mise à jour
        print(numbers)
    else:
        print("Invalid index. Please try again.")

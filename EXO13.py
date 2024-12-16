def print_underlined_strings():
    while True:
        # Demander à l'utilisateur de saisir une chaîne
        user_input = input("Please type in a string: ")

        # Si la chaîne est vide, sortir de la boucle
        if user_input == "":
            break
        
        # Afficher la chaîne et la souligner
        print(user_input)
        print("-" * len(user_input))

# Appeler la fonction principale
if __name__ == "__main__":
    print_underlined_strings()

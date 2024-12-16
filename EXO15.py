def check_vowels_in_string():
    # Demander à l'utilisateur de saisir une chaîne en minuscules
    user_input = input("Please type in a string: ")

    # Liste des voyelles à vérifier
    vowels = ['a', 'e', 'o']

    # Vérification de chaque voyelle
    for vowel in vowels:
        if vowel in user_input:
            print(f"{vowel} found")
        else:
            print(f"{vowel} not found")

# Appeler la fonction principale
if __name__ == "__main__":
    check_vowels_in_string()

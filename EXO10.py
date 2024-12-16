def check_palindrome():
    # Demander à l'utilisateur de saisir un mot
    word = input("Please type a word: ")

    is_palindrome = True  # Initialiser la variable à True

    # Boucle à travers la première moitié du mot
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            is_palindrome = False  # Si les caractères ne correspondent pas, c'est un palindrome
            break  # Sortir de la boucle

    # Afficher le résultat en fonction de la variable is_palindrome
    if is_palindrome:
        print("Yes, it's a palindrome.")
    else:
        print("No, it's not a palindrome.")

# Appeler la fonction principale
if __name__ == "__main__":
    check_palindrome()

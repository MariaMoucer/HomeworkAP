def print_frame_with_word():
    # Demander à l'utilisateur de saisir une chaîne
    word = input("Word: ")

    # Largeur du cadre
    frame_width = 30

    # Calculer les espaces nécessaires avant et après le mot pour le centrer
    spaces = (frame_width - len(word)) // 2

    # Créer la ligne du cadre avec le mot centré
    frame_line = ' ' * spaces + word + ' ' * (frame_width - len(word) - spaces)

    # Afficher la ligne avec le mot et les étoiles
    print('*' * frame_width)
    print(frame_line + '*')
    print('*' * frame_width)

# Appeler la fonction principale
if __name__ == "__main__":
    print_frame_with_word()

def print_hash_rectangle():
    # Demander à l'utilisateur de saisir la largeur et la hauteur
    width = int(input("Width: "))
    height = int(input("Height: "))

    # Imprimer le rectangle de '#' en fonction de la largeur et de la hauteur
    for _ in range(height):
        print('#' * width)

# Appeler la fonction principale
if __name__ == "__main__":
    print_hash_rectangle()

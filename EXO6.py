def separate_dinars_and_centimes():
    # Demander à l'utilisateur de saisir un prix
    price = float(input("Please type in a price: "))

    # Extraire les dinars (partie entière) et les centimes (partie décimale)
    dinars = int(price)  # Convertir en entier pour obtenir les dinars
    centimes = round((price - dinars) * 100)  # Calculer les centimes

    # Afficher les résultats
    print(f"Dinars: {dinars}")
    print(f"Centimes: {centimes}")

# Appeler la fonction principale
if __name__ == "__main__":
    separate_dinars_and_centimes()

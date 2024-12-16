def calculate_discounted_price():
    # Demander les entrées à l'utilisateur
    total_amount = float(input("Total amount: "))
    number_of_items = int(input("Number of items: "))
    day_of_week = input("Day of the week: ").strip().capitalize()

    # Appliquer la remise selon le jour de la semaine
    discount = 0
    if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        discount += 10  # 10% pour les jours de semaine
    elif day_of_week in ["Saturday", "Sunday"]:
        discount += 20  # 20% pour les week-ends

    # Appliquer une remise supplémentaire si le nombre d'articles > 5
    if number_of_items > 5:
        discount += 5  # Remise supplémentaire de 5%

    # Calculer le prix total après remise
    discounted_price = total_amount * (1 - discount / 100)

    # Afficher le résultat
    print(f"Total price after discount: {discounted_price:.1f} dinars")

# Appeler la fonction principale
if __name__ == "__main__":
    calculate_discounted_price()

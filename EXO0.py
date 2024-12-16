def calculate_taxis_needed():
    # Demander à l'utilisateur combien de personnes ont besoin d'un taxi
    people = int(input("How many people need a ride? "))
    
    # Demander combien de personnes peuvent entrer dans un taxi
    capacity = int(input("How many people fit in one taxi? "))
    
    # Calculer le nombre de taxis nécessaires
    taxis = people // capacity
    if people % capacity != 0:  # Vérifier s'il reste des personnes pour un taxi supplémentaire
        taxis += 1
    
    # Afficher le résultat
    print(f"Number of taxis needed: {taxis}")

# Appeler la fonction principale
if __name__ == "__main__":
    calculate_taxis_needed()

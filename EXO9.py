def city_population():
    cities = []

    # Demander à l'utilisateur de saisir les villes
    while True:
        city_name = input("Enter a city name (or type 'stop' to end): ")
        if city_name.lower() == 'stop':
            break
        # Calculer la population en fonction de la longueur du nom de la ville
        population = len(city_name) * 1000000
        cities.append((city_name, population))

    # Trier les villes par population (du plus grand au plus petit)
    cities.sort(key=lambda city: city[1], reverse=True)

    # Afficher les villes et leurs populations
    print("\nCities sorted by population:")
    for city in cities:
        print(f"{city[0]}: {city[1]} citizens")

# Appeler la fonction principale
if __name__ == "__main__":
    city_population()

def determine_faster_runner():
    # Entrées pour le coureur 1
    print("Runner 1:")
    name1 = input("Name: ")
    time1 = float(input("Time (in seconds): "))
    
    # Entrées pour le coureur 2
    print("Runner 2:")
    name2 = input("Name: ")
    time2 = float(input("Time (in seconds): "))
    
    # Comparaison des temps et affichage des résultats
    if time1 < time2:
        print(f"The faster runner is {name1}")
    elif time2 < time1:
        print(f"The faster runner is {name2}")
    else:
        print(f"{name1} and {name2} have the same time")

# Appeler la fonction principale
if __name__ == "__main__":
    determine_faster_runner()

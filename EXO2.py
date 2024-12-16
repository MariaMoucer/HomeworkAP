def temperature_warnings():
    # Demander la température à l'utilisateur
    temperature = int(input("Please type in the temperature: "))
    
    # Vérifier les conditions et afficher les messages correspondants
    if temperature < 0:
        print("It's freezing!")
    if temperature < 10:
        print("It's cold!")
    if temperature < 20:
        print("It's cool!")
    
    # Toujours terminer avec "Stay safe!"
    print("Stay safe!")

# Appeler la fonction principale
if __name__ == "__main__":
    temperature_warnings()

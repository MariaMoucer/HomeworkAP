def fizz_buzz():
    # Demander à l'utilisateur de saisir un nombre entier
    number = int(input("Number: "))

    # Vérifier si le nombre est divisible par 3 et/ou 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        pass  # Si le nombre n'est divisible ni par 3 ni par 5, rien n'est affiché

# Appeler la fonction principale
if __name__ == "__main__":
    fizz_buzz()

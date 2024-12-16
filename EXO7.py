def check_leap_year():
    # Demander à l'utilisateur de saisir une année
    year = int(input("Please type in a year: "))

    # Vérifier si l'année est bissextile
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")

# Appeler la fonction principale
if __name__ == "__main__":
    check_leap_year()

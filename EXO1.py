def ticket_purchase_system():
    # Demander le nom de l'utilisateur
    name = input("Please enter your name: ")
    
    if name == "VIP":
        # Si le nom est "VIP", ils profitent gratuitement du spectacle
        print("Enjoy the show for free!")
    else:
        # Sinon, demander combien de billets l'utilisateur veut acheter
        tickets = int(input("How many tickets would you like to buy? "))
        ticket_price = 15.50  # Prix par billet
        total_cost = tickets * ticket_price  # Calculer le coût total
        print(f"The total cost is {total_cost}")
        print("Enjoy your tickets!")

# Appeler la fonction principale
if __name__ == "__main__":
    ticket_purchase_system()

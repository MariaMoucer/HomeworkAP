# Function to handle invalid inputs and ask for a valid positive integer
def get_positive_integer():
    while True:
        try:
            # Ask the user for a positive integer
            N = int(input("Please enter a positive integer: "))
            # Check if the number is positive
            if N <= 0:
                print("Please enter a positive integer.")
            else:
                return N
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Get the valid positive integer N
N = get_positive_integer()

# Print numbers from -N to N (excluding 0)
for i in range(-N, N + 1):
    if i != 0:
        print(i)

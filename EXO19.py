# Initialize an empty set to store unique words
unique_words = set()

# Continuously prompt the user for words
while True:
    # Ask the user for a word and strip leading/trailing whitespace
    word = input("Enter a word: ").strip()

    # Check if the word is already in the set of unique words
    if word in unique_words:
        # If a duplicate is found, print the count of unique words and exit
        print(f"You typed in {len(unique_words)} unique words.")
        break
    else:
        # If the word is not a duplicate, add it to the set
        unique_words.add(word)

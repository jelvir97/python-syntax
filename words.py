word_list = ['apple','banana','grapefruit','orange','plum']

def print_upper_words(words, *starting_let):
    for word in words:
        for letter in starting_let:
            if word.casefold().startswith(letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes","elephant"],"e", "g",'y')
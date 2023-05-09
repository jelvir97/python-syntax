word_list = ['apple','banana','grapefruit','orange','plum']

def print_upper_words(words, *starting_let):
    """ Accepts list and starting character
        -sorts through list, ignoring case, finding elements that start 
        with given letters
        -prints out selected words in UPPERCASE
    """

    for word in words:
        for letter in starting_let:
            if word.casefold().startswith(letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes","elephant"],"e", "g",'y')
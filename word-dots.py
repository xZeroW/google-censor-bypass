def add_dots(word):
    # Combining dot below (U+0323) and combining dot above (U+0307)
    dot_below = '\u0323'
    dot_above = '\u0307'

    # Add dots to each character in the word
    dotted_word = ''.join([char + dot_below + dot_above for char in word])

    return dotted_word

# Get user input
input_word = input("Enter a word: ")

# Output the word with dots
output_word = add_dots(input_word)
print(output_word)

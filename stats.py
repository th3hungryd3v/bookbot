def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_counts = {} # empty dict
    text = text.lower() # convert all chars to lowercase

    for char in text: # iterate each char
        if char in char_counts: # check if the character is already in the dict
            char_counts[char] += 1 # add 1 if it exists
        else:
            char_counts[char] = 1 # add char to dict with a count of 1
    return char_counts

def sort_counts(char_counts):
    # Docstring!
    sorted_counts = []
    
    for char, count in char_counts.items():
        if char.isalpha(): # Just letters of the alphabet
            sorted_counts.append({'char': char, 'count': count}) # add alpha to sorted counts using these keys/value pairs

    sorted_counts.sort(key=lambda item: item['count'], reverse=True)
    return sorted_counts

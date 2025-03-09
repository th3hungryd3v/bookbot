def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    store = {} # empty dict
    text = text.lower() # convert all chars to lowercase

    for char in text: # iterate each char
        if char in store: # check if the character is already in the dict
            store[char] += 1 # add 1 if it exists
        else:
            store[char] = 1 # add char to dict with a count of 1
    return store
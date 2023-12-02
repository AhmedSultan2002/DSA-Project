def word_id_generator():
    mapping_words_to_id = {}
    current_word_id = 0

    # Function to return the ID of a word
    def get_word_id(word):
        nonlocal current_word_id  

        #If the current word id is not yet mapped then we assign that Id to our word and increment it
        if word not in mapping_words_to_id:
            mapping_words_to_id[word] = current_word_id
            current_word_id += 1
        #Returning the Assigned ID
        return mapping_words_to_id[word]
    return get_word_id
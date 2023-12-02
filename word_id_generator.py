def word_id_generator(word, word_list):
    existing_word_ids = {existing_word["id"] for existing_word in word_list}

    new_word_id = 0
    
    # Increment the new word ID until a unique ID is found
    while new_word_id in existing_word_ids:
        new_word_id =new_word_id+ 1

    return new_word_id
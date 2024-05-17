import json
from glob import glob
import os

def inverted_func():
    # Implementing word id dictionary, basically the content of the inverted index
    wordid_dict = {}

    # Accessing all forward indexes
    Fwd_indexes = glob(os.path.join('Resources', 'fwd_indexes', '*'))
    for index_file in Fwd_indexes:
        with open(index_file, 'r') as cur_file:
            cur_index_json = json.load(cur_file)  # Loading the contents of current fwd_index
            for item in cur_index_json:  # Accessing each Article
                for word in item["words"]:  # Accessing each word in word list associated with article
                    word_id = int(word['id'])  # Taking word id, url, and count out from each word
                    url = item["URL"]
                    count = word["count"]

                    if word_id not in wordid_dict:  # Checking if this id has already been added to the dictionary
                        wordid_dict[word_id] = {}  # If not added, initialize empty dictionary as value for wordid

                    # Add the current url as the key for dictionary associated with word id with the value associated being count
                    wordid_dict[word_id][url] = count

    # Writing the inverted index to a file
    file_path = os.path.join('Resources', 'inv_index', 'inv_index.json')
    with open(file_path, 'w') as inv_index:
        json.dump(wordid_dict, inv_index, indent=0)

inverted_func()

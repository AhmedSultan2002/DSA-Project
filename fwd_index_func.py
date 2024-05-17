import json
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from stop_words import get_stop_words
import copy
import word_id_generator as WID
import os

# Parsing function: loads file_path into a variable, uses said filepath to open a file,
# loads that file into a json object, which is then further used to get needed values from the list.

def FWD_index_parsing(file_path, index_path, word_func):
    word_dict = {"id": 0, "count": 0, "word_name": " "}
    list_of_words = []
    Doc_dict = {
        "title": " ",
        "URL": " ",
        "words": list_of_words
    }
    article_list = []

    with open(file_path, 'r') as file:
        json_file = json.load(file)  # Loading json file
        for file in json_file:  # To go over every article in json file
            curr_content = file['content'].lower()
            translator = str.maketrans("", "", string.punctuation)
            curr_content = curr_content.translate(translator)
            unnecessary_char = ['’', "“", "”", "‘"]  # Cleaning string of any punctuation or unwanted characters
            for char in unnecessary_char:
                curr_content = curr_content.replace(char, "")

            title_string = file['title'].lower()
            title_words = word_tokenize(title_string)
            separated_words = word_tokenize(curr_content)  # Tokenizing content into word list

            stop_words_set = set(get_stop_words("en"))
            separated_words_no_stop_words = []
            title_words_no_stop_words = []

            for word in separated_words:  # Removing stop words from word list
                if word.lower() not in stop_words_set:
                    separated_words_no_stop_words.append(word)

            for title_word in title_words:
                if title_word.lower() not in stop_words_set:
                    title_words_no_stop_words.append(title_word)

            word_list = []  # Initializing list of words dictionary
            separated_words_no_stop_words.extend(title_words_no_stop_words)  # Combining title words into larger content words list

            for word1 in set(separated_words_no_stop_words):
                cur_word = word_dict.copy()  # Splitting words into words and word counts and inputting that into dictionaries
                cur_word.update({"id": word_func(word1)})
                cur_word.update({"count": separated_words_no_stop_words.count(word1)})  # Adding them to a list of words and word counts
                cur_word.update({"word_name": word1})
                if word1 in set(title_words_no_stop_words):
                    cur_word.update({"count": separated_words_no_stop_words.count(word1) + 20})
                word_list.append(cur_word.copy())

            cur_doc = Doc_dict.copy()
            cur_doc.update({"title": file["title"]})  # Adding list to a dictionary of doc, which includes title, URL, and list of word dictionaries
            cur_doc.update({"URL": file["url"]})
            cur_doc.update({"words": word_list})

            article_list.append(cur_doc)

        # Writes the entire article list into a json
        try:
            with open(index_path, 'r') as read_file:  # Reading from existing Fwd_index
                data = json.load(read_file)
                data.extend(article_list)
        except json.JSONDecodeError:
            data = []
            data.extend(article_list)

        with open(index_path, 'w') as write_file:  # Appending and writing to update_Fwd index
            json.dump(data, write_file, indent=0)

# Example usage
file_path = os.path.join('Resources', 'some_file.json')
index_path = os.path.join('Resources', 'fwd_index', 'index.json')
word_func = WID.word_id_generator({})  # Replace with actual word function
FWD_index_parsing(file_path, index_path, word_func)

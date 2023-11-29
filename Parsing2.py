import json
import string
# using nltk to separate words and remove stop words from wordlist
from nltk import  word_tokenize
from nltk.corpus import stopwords
from stop_words import get_stop_words

#parsing function, loads file_path into a variable, uses said filepath to open a file, loads that file into a json object, which is then further used to 
#get needed values from the list.

file_path1 = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\nela-gt-2022\newsdata\369news.json"
def parsing(file_path):
    with open (file_path, 'r') as file:
        json_file = json.load(file)                             
        curr_content = json_file[0]['content']                  
        translator = str.maketrans("", "", string.punctuation)  #
        curr_content = curr_content.translate(translator)       #
        unnecessary_char = ['’',"“","”","‘"]                    # Cleaning string of any punctuation or unwanted characters
        for char in unnecessary_char:                           #
            curr_content = curr_content.replace(char, "")       #


        separated_words = word_tokenize(curr_content)           # Tokenizing content into word list
        


        stop_words2 = set(get_stop_words("en"))                 #
        separated_words2 = []                                   #
        for word in separated_words:                            # Removing stop words from word list
           if  not word.lower() in stop_words2:                 # 
                separated_words2.append(word)                   #

        
        for word in set(separated_words2):
            print(word + "," + str(separated_words2.count(word)))   # splitting words into words and word counts
        
    
        
                                                                
           
        


        




parsing(file_path1)


import json
import os
import lexicon as lx

#parsing function, loads file_path into a variable, uses said filepath to open a file, loads that file into a json object, which is then further used to 
#get needed values from the list.

file_path1 = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\nela-gt-2022\newsdata\369news.json"
def parsing(file_path):
    with open (file_path, 'r') as file:
        json_file = json.load(file)
        print(json_file[0]['title'])
        print(json_file[0]['url'])
        content = json_file[0]['content']
        wordList = content.split()

        print(wordList)




parsing(file_path1)


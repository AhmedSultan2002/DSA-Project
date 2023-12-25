import json
from nltk import word_tokenize
import word_id_generator as WID




def Search_func(query):
    word_dict = {}
    filepath = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\Word_Dictionary\lexicon.json"
    with open(filepath, 'r') as dic_file:
        word_dict = json.load(dic_file)

    
    word_func = WID.word_id_generator(word_dict)

    separated_query = word_tokenize(query)
    
    if len(separated_query) == 1:
        wor_id = word_func(separated_query[0].lower())
        filepath = f"D:\\Vscode\\NUST\\Semester 3\\DSA2\\DSA-Project\\Resources\\inv_index\\barrel_{wor_id//500}.json"
        with open(filepath, 'r') as current_barrel:
            loaded_barrel = json.load(current_barrel)
            #print(loaded_barrel[str(wor_id)])
            #print(loaded_barrel)
            id_dict = loaded_barrel[str(wor_id)]
            top_10_URLs = sorted(id_dict, key=id_dict.get, reverse=True)[:10]
            for url in top_10_URLs:
                print(url)


                








Search_func("lucifer")



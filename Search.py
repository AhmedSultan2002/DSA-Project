import json
from nltk import word_tokenize
import word_id_generator as WID
import heapq



def Search_func(query):
    word_dict = {}
    filepath = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\Word_Dictionary\lexicon.json"
    with open(filepath, 'r') as dic_file:
        word_dict = json.load(dic_file)

    
    word_func = WID.word_id_generator(word_dict)
    separated_query = word_tokenize(query)
    #print(separated_query)
    URL_heap = []
    
    if len(separated_query) == 1:
        wor_id = word_func(separated_query[0].lower())
        filepath = f"D:\\Vscode\\NUST\\Semester 3\\DSA2\\DSA-Project\\Resources\\inv_index\\barrel_{wor_id//500}.json"
        with open(filepath, 'r') as current_barrel:
            loaded_barrel = json.load(current_barrel)
            id_dict = loaded_barrel[str(wor_id)]
            top_10_URLs = sorted(id_dict, key=id_dict.get, reverse=True)[:10]
            return top_10_URLs
    elif len(separated_query) == 0:
        return ["Please Enter correct search query"]
    else:
        URLs_List_in_order = []
        for word in separated_query:
            wor_id = word_func(word)
            #print(wor_id)
            filepath = f"D:\\Vscode\\NUST\\Semester 3\\DSA2\\DSA-Project\\Resources\\inv_index\\barrel_{wor_id//500}.json"
            with open(filepath, 'r') as current_barrel:
                loaded_barrel = json.load(current_barrel)
                id_dict = loaded_barrel[str(wor_id)]
                for key, value in id_dict.items():
                    heapq.heappush(URL_heap, (-value, key))
            while URL_heap:
                value, key = heapq.heappop(URL_heap)
                URLs_List_in_order.append(key)
        return URLs_List_in_order
        





        
ToDisplay = Search_func("lucifer bomb")
for stuff in ToDisplay:
    print(stuff)




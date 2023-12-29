import json
from nltk import word_tokenize
import word_id_generator as WID
import heapq



def Search_func(query):
    word_dict = {}
    filepath = r"Resources\Word_Dictionary\lexicon.json"
    with open(filepath, 'r') as dic_file:
        word_dict = json.load(dic_file)

    
    word_func = WID.word_id_generator(word_dict)
    separated_query = word_tokenize(query)
    #print(separated_query)
    URL_heap = []
    
    if len(separated_query) == 1:                    #Case if it is a single word query
        wor_id = word_func(separated_query[0].lower())
        filepath = f"Resources\\inv_index\\barrel_{wor_id//10}.json"  #Get wordid of query from lexicon function, and use that to open corresponding barrel
        with open(filepath, 'r') as current_barrel:
            loaded_barrel = json.load(current_barrel)
            id_dict = loaded_barrel[str(wor_id)]
            top_10_URLs = sorted(id_dict, key=id_dict.get, reverse=True)[:10] #return the 10 highest count URLS from that barrel associated with that wordid
            return top_10_URLs  #return them as a list
    elif len(separated_query) == 0:     
        return ["Please Enter correct search query"]
    else:  #Case of multiword Query.
        URLs_List_in_order = []                                            #list of urls which will be returned
        for word in separated_query:
            wor_id = word_func(word.lower())                                       #similar to before get word id for each word one by one
            filepath = f"Resources\\inv_index\\barrel_{wor_id//10}.json"  #Open corresponding barrel to find URLS
            with open(filepath, 'r') as current_barrel:
                loaded_barrel = json.load(current_barrel)
                id_dict = loaded_barrel[str(wor_id)]
                for key, value in id_dict.items():
                    heapq.heappush(URL_heap, (-value, key))                #push the URLS based on value into a max Heap, for effective storage and retreival
        while URL_heap:
            value, key = heapq.heappop(URL_heap)                           #pop all URLS from heap one by one and add them to List in then highest rank order
            URLs_List_in_order.append(key)  
        
        URLs_list_in_order_no_duplicates = []
        URLs_list_in_order_no_duplicates = [url for url in URLs_List_in_order if url not in URLs_list_in_order_no_duplicates] #remove duplicates
        top_20_URLs = URLs_list_in_order_no_duplicates[:20]                #get 20 best results
        return top_20_URLs                                                 #return results
        





        
ToDisplay = Search_func("lucifer bomb assault")
for stuff in ToDisplay:
    print(stuff)




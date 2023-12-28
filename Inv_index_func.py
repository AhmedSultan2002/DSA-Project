import json
from glob import glob


def inverted_func():
    #article_dic = {}
    wordid_dict = {}        #impleneting word id dictionary, basically the content of the inverted index


    Fwd_indexes = glob(r"Resources\fwd_indexes\*")   #Accessing all forward indexes
    for index_file in Fwd_indexes:
        with open(index_file, 'r') as cur_file:
            cur_index_json = json.load(cur_file)                            #loading the contents of current fwd_index
            for item in cur_index_json:                                     #accessing each Article
                for word in item["words"]:                                  #accessing each word in word list associated with article
                    word_id = int(word['id'])                               #taking word id, url and count out from each word
                    url = item["URL"]           
                    count = word["count"]
                    

                    if word_id not in wordid_dict:                          #checking if this id has already been added to the dictionary
                        wordid_dict[word_id] = {}                           #if not added initialize empty dictionary as value for wordid
                    
                    wordid_dict[word_id][url] = count                       #add the current url as the key for dictionary assocaited with word id with the value associated being count

    

    file_path = r"Resources\inv_index\inv_index.json"
    with open(file_path, 'w') as inv_index:
        json.dump(wordid_dict, inv_index, indent=0)                         #finally writing this to make inverted index



inverted_func()


        

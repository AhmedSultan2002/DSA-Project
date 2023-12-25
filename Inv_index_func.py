import json
from glob import glob


def inverted_func():
    #article_dic = {}
    wordid_dict = {}


    Fwd_indexes = glob(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\fwd_indexes\*")
    for index_file in Fwd_indexes:
        with open(index_file, 'r') as cur_file:
            cur_index_json = json.load(cur_file)
            for item in cur_index_json:
                for word in item["words"]:
                    word_id = int(word['id'])
                    url = item["URL"]
                    count = word["count"]
                    

                    if word_id not in wordid_dict:
                        wordid_dict[word_id] = {}
                    
                    wordid_dict[word_id][url] = count

    

    file_path = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\inv_index\inv_index.json"
    with open(file_path, 'w') as inv_index:
        json.dump(wordid_dict, inv_index, indent=0)



inverted_func()


        

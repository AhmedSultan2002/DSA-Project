import json
from glob import glob


def inverted_func():
    article_dic = {"url" : " ", "count" : 0 }
    wordid_dict = {}


    Fwd_indexes = glob(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\fwd_indexes\*")
    for index_file in Fwd_indexes:
        with open(index_file, 'r') as cur_file:
            cur_index_json = json.load(cur_file)
            for item in cur_index_json:
                for word in item["words"]:
                    word_id = word['id']
                    article_dic = {"url": item["URL"], "count": word["count"]}
                    

                    if word_id in wordid_dict:
                        articles_already_listed = wordid_dict[word_id]
                        if article_dic not in articles_already_listed:
                            articles_already_listed.append(article_dic)
                    else:
                        wordid_dict[word_id] = [article_dic]

    

    file_path = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\inv_index\inv_index_test.json"
    with open(file_path, 'w') as inv_index:
        json.dump(wordid_dict, inv_index, indent =2)



inverted_func()


        

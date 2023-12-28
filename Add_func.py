import json
import Add_func_dependencies as AFD
import word_id_generator as WID

def add_file_func(JsonFileContent):
    word_dict = {}
    filepath = r"Resources\fwd_indexes\New_file.json"
    word_dict_path = r"Resources\Word_Dictionary\lexicon.json"
    
    with open(word_dict_path, 'r') as wr_dic_file:
        word_dict = json.load(wr_dic_file)
    
    word_func = WID.word_id_generator(word_dict)

    AFD.FWD_index_parsing(JsonFileContent, filepath, word_func)
    AFD.inverted_func(filepath)

    newfilePath = r"Resources\inv_index\new_inv_index.json"
    with open(newfilePath) as inv_index:
        inv_index_content = json.load(inv_index)
        ids = list(inv_index_content.keys())
        barrel_content = {}
        for key_id in ids:
            barrelpath = f"Resources/inv_index/barrel_{int(key_id)//500}.json"
            #print(int(key_id)//500)
            with open(barrelpath, 'r') as reading_barrel:
                barrel_content = json.load(reading_barrel)
                if key_id not in barrel_content:
                    barrel_content[key_id] = {}
                    barrel_content[key_id] = inv_index_content[key_id]
                else:
                    barrel_content[key_id].update(inv_index_content[key_id])
            with open(barrelpath, 'w') as replacing_barrel:
                json.dump(barrel_content, replacing_barrel, indent=2)


#testing add function
#filepath = r"Resources\nela-gt-2022\newsdata\369news.json"
#with open(filepath, 'r') as testJson:
#    content = json.load(testJson)
#    add_file_func(content)
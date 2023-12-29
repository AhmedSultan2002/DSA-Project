import json
import Add_func_dependencies as AFD
import word_id_generator as WID

def add_file_func(JsonFilePath):
    word_dict = {}
    index_filepath = r"Resources\fwd_indexes\New_file.json"   #path of fwd index that will be created always
    word_dict_path = r"Resources\Word_Dictionary\lexicon.json" #path of lexicon
    
    with open(word_dict_path, 'r') as wr_dic_file:
        word_dict = json.load(wr_dic_file)
    
    word_func = WID.word_id_generator(word_dict)

    AFD.FWD_index_parsing(JsonFilePath, index_filepath, word_func)  #create forward index from article
    AFD.inverted_func(index_filepath)                               #create inverted index from article

    newfilePath = r"Resources\inv_index\new_inv_index.json" #path of inverted index that will be created always
    with open(newfilePath) as inv_index:
        inv_index_content = json.load(inv_index)
        ids = list(inv_index_content.keys())
        barrel_content = {}
        for key_id in ids:
            barrelpath = f"Resources/inv_index/barrel_{int(key_id)//10}.json"      #browse through new inverted index getting one wordid at a time
            with open(barrelpath, 'r') as reading_barrel:                           #then using wordid open corresponding barrel and update the associated
                barrel_content = json.load(reading_barrel)
                if key_id in barrel_content:                                    #word id dictionary in that article
                    barrel_content[key_id].update(inv_index_content[key_id])            #using Update as it will create dictionary there if it doesnt exist and if it exists it will simply update it.
                else:
                    barrel_content[key_id] = {}
                    barrel_content[key_id].update(inv_index_content[key_id])
            with open(barrelpath, 'w') as replacing_barrel:
                json.dump(barrel_content, replacing_barrel, indent=0)


#testing add function
filepath = r"Resources\nela-gt-2022\newsdata\369news.json"
add_file_func(filepath)
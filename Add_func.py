import json
import Add_func_dependencies as AFD
import word_id_generator as WID
import os

def add_file_func(JsonFilePath):
    word_dict = {}

    # Use os.path.join for cross-platform compatibility
    index_filepath = os.path.join('Resources', 'fwd_indexes', 'New_file.json')  # Path of fwd index that will be created always
    word_dict_path = os.path.join('Resources', 'Word_Dictionary', 'lexicon.json')  # Path of lexicon

    with open(word_dict_path, 'r') as wr_dic_file:
        word_dict = json.load(wr_dic_file)

    word_func = WID.word_id_generator(word_dict)

    AFD.FWD_index_parsing(JsonFilePath, index_filepath, word_func)  # Create forward index from article
    AFD.inverted_func(index_filepath)  # Create inverted index from article

    newfilePath = os.path.join('Resources', 'inv_index', 'new_inv_index.json')  # Path of inverted index that will be created always
    with open(newfilePath, 'r') as inv_index:
        inv_index_content = json.load(inv_index)
        ids = list(inv_index_content.keys())
        for key_id in ids:
            barrel_content = {}
            barrelpath = os.path.join('Resources', 'inv_index', f'barrel_{int(key_id)//10}.json')  # Browse through new inverted index getting one wordid at a time
            with open(barrelpath, 'r') as reading_barrel:  # Then using wordid open corresponding barrel and update the associated
                barrel_content = json.load(reading_barrel)
                barrel_content[key_id].update(inv_index_content[key_id])  # Word id dictionary in that article
            with open(barrelpath, 'w') as replacing_barrel:
                json.dump(barrel_content, replacing_barrel)

# Testing add function
filepath = os.path.join('Resources', 'nela-gt-2022', 'newsdata', '369news.json')
add_file_func(filepath)

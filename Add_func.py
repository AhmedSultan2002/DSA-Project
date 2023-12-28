import json
import Add_func_dependencies as AFD
from Inv_index_func import inverted_func as IF
from Barrel_Func import Barrel_func as BF
import word_id_generator as WID

def add_file_func(JsonFileContent):
    word_dict = {}
    filepath = r"C:\Users\emanm\.vscode\DSA-Project\Search-Engine\Resources\nela-gt-2022\newsdata"
    word_dict_path = r"C:\Users\emanm\.vscode\DSA-Project\Search-Engine\Resources\Word_Dictionary\lexicon.json"
    
    with open(word_dict_path, 'r') as wr_dic_file:
        word_dict = json.load(wr_dic_file)
    
    word_func = WID.word_id_generator(word_dict)

    AFD.FWD_index_parsing(JsonFileContent, filepath, word_func)
    AFD.inverted_func(filepath)

    newfilePath = r"C:\Users\emanm\.vscode\DSA-Project\Search-Engine\Resources\inv_index\new_inv_index.json"
    with open(newfilePath) as inv_index:
        inv_index_content = json.load(inv_index)
        ids = list(inv_index_content.keys())
        for key_id in ids:
            barrelpath = "input barrel path here"
            barrel_content = {}
            with open(barrelpath, 'r') as reading_barrel:
                barrel_content = json.load(reading_barrel)
                barrel_content[int(key_id)].update(inv_index[key_id])


    

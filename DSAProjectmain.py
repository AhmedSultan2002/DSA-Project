import fwd_index_func as FW
from glob import glob
import word_id_generator as WID
import json




word_dict = {}
word_func = WID.word_id_generator(word_dict)
Jsons = glob(r"Resources\nela-gt-2022\newsdata\*")
Indexes = glob(r"Resources\fwd_indexes\*")


for Json, fwIndex_path in zip(Jsons, Indexes):
    FW.FWD_index_parsing(Json, fwIndex_path, word_func)


Dictionary_path = r"Resources\Word_Dictionary\lexicon.json"
with open(Dictionary_path, 'w') as dictionary_write:
    json.dump(word_dict, dictionary_write, indent=0)






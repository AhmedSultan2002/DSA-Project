import fwd_index_func as FW
from glob import glob
import word_id_generator as WID
import json
import os

word_dict = {}
word_func = WID.word_id_generator(word_dict)

# Use os.path.join for cross-platform compatibility
Jsons = glob(os.path.join('Resources', 'nela-gt-2022', 'newsdata', '*'))
Indexes = glob(os.path.join('Resources', 'fwd_indexes', '*'))

for Json, fwIndex_path in zip(Jsons, Indexes):
    FW.FWD_index_parsing(Json, fwIndex_path, word_func)

Dictionary_path = os.path.join('Resources', 'Word_Dictionary', 'lexicon.json')
with open(Dictionary_path, 'w') as dictionary_write:
    json.dump(word_dict, dictionary_write, indent=0)

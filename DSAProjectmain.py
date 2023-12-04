import fwd_index_func as FW
from glob import glob
import word_id_generator as WID


Jsons = glob(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\nela-gt-2022\newsdata\*")
Indexes = glob(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\fwd_indexes\*")

#for Json, fwIndex_path in zip(Jsons, Indexes):
 #   FW.FWD_index_parsing(Json, fwIndex_path)


#TEST

json_path = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\nela-gt-2022\newsdata\369news.json"
index_path = r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\fwd_indexes\Fwd_index02.json"
word_func = WID.word_id_generator()

FW.FWD_index_parsing(json_path, index_path, word_func)


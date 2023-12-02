import fwd_index_func as FW
from glob import glob



Jsons = glob(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\nela-gt-2022\newsdata\*")
Indexes = glob(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\fwd_indexes\*")

for Json, fwIndex_path in zip(Jsons, Indexes):
    FW.FWD_index_parsing(Json, fwIndex_path)



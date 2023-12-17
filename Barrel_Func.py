import json



def Barrel_func(file_path):
    barrel_size = 500
    with open(file_path, 'r') as full_index:
        index_data = json.load(full_index)


        ids = list(index_data.keys())
        for i in range(0, len(ids), barrel_size):
            barrel = {id : index_data[id] for id in ids[i:i + barrel_size]}


            with open(f"D:/Vscode/NUST/Semester 3/DSA2/DSA-Project/Resources/inv_index/barrel_{i//barrel_size}.json", 'w') as cur_barrel:
                json.dump(barrel, cur_barrel, indent = 2)







Barrel_func(r"D:\Vscode\NUST\Semester 3\DSA2\DSA-Project\Resources\inv_index\inv_index.json")




import json



def Barrel_func(file_path):
    barrel_size = 500                           #amount of ids in each barrel
    with open(file_path, 'r') as full_index:
        index_data = json.load(full_index)   #load inverted index


        ids = list(index_data.keys())
        for i in range(0, len(ids), barrel_size):
            barrel = {id : index_data[id] for id in ids[i:i + barrel_size]}  #splice according to ids


            with open(f"Resources/inv_index/barrel_{i//barrel_size}.json", 'w') as cur_barrel:  #create custom barrel number based on i which will start at 0
                json.dump(barrel, cur_barrel, indent = 2)







Barrel_func(r"Resources\inv_index\inv_index.json")




import json
import os

def Barrel_func(file_path):
    barrel_size = 10  # Amount of ids in each barrel
    with open(file_path, 'r') as full_index:
        index_data = json.load(full_index)  # Load inverted index

        ids = list(index_data.keys())
        for i in range(0, len(ids), barrel_size):
            barrel = {id: index_data[id] for id in ids[i:i + barrel_size]}  # Splice according to ids

            barrel_path = os.path.join('Resources', 'inv_index', f'barrel_{i//barrel_size}.json')
            with open(barrel_path, 'w') as cur_barrel:  # Create custom barrel number based on i which will start at 0
                json.dump(barrel, cur_barrel)

# Define file path using os.path.join for cross-platform compatibility
file_path = os.path.join('Resources', 'inv_index', 'inv_index.json')
Barrel_func(file_path)

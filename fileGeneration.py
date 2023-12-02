import json
import os

num_files = 36

def create_empty_json_files(folder_path, num_files):
    file_names = [f'Fwd_index{i:02d}.json' for i in range(1, num_files + 1)]    
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as json_file:
            # Writing an empty JSON object {}
            json.dump([], json_file)

# Example usage
folder_path = 'DSA-Project/Resources/fwd_indexes'
num_files = 36

create_empty_json_files(folder_path, num_files)


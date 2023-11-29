import os
import codecs
import json

for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        json_file_path = os.path.join(folder_path, file_name)
        output_file_path = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}_output.txt")

        try:
            with codecs.open(json_file_path, 'r', 'utf-8') as json_file:
                all_data = json.load(json_file)

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(f"# Parsed data from {json_file_path}\n\n")

                for data_item in all_data:
                    output_file.write("Title: " + str(data_item["title"]) + "\n")
                    output_file.write("Date: " + str(data_item["date"]) + "\n")
                    output_file.write("Source: " + str(data_item["source"]) + "\n")
                    output_file.write("Content: " + str(data_item["content"]) + "\n")
                    output_file.write("Author: " + str(data_item["author"]) + "\n")
                    output_file.write("URL: " + str(data_item["url"]) + "\n")
                    output_file.write("Published: " + str(data_item["published"]) + "\n\n")

        except Exception as e:
            print(f"Error processing {json_file_path}: {e}")

import os
import json
import csv

folder_path = 'AllCountries'

json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# Initialize an empty list to store JSON data
data_list = []

for json_file in json_files:
    file_path = os.path.join(folder_path, json_file)

    with open(file_path, 'r') as f:
        json_data = json.load(f)        

        country = json_data['country']
        country_code = json_data['country_code']

        for row in json_data['list']:
            row['country'] = country
            row['country_code'] = country_code
            data_list.append(row)

csv_file_path = 'AllCountries.csv'
fieldnames = data_list[0].keys()

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)
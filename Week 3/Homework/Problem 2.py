import pathlib
import json
import csv
import os
import time

target = pathlib.Path('pathsfound.json')

with open(target, 'r') as file_in:
    data = json.load(file_in)

all_rows = []

for file_path in data['files']:
    file_path = pathlib.Path(file_path)
    last_modification_time = os.path.getmtime(file_path)
    converted_last_modification_time = time.strftime("%Y-%m-%d", time.gmtime(last_modification_time))
    file_name = file_path.name
    one_row = [converted_last_modification_time, file_name]
    all_rows.append(one_row)

headers = ['last_edited_date', 'filename']

with open(pathlib.Path('editeddate.csv'), 'w') as file_out:
    csv_out = csv.writer(file_out)
    csv_out.writerow(headers)
    csv_out.writerows(all_rows)

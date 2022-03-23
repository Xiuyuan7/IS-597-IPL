import pathlib
import shutil
import sqlite3
import json
import csv

shutil.unpack_archive('records.zip')

target = pathlib.Path('records')
json_files = list(target.glob('*.json'))

database = pathlib.Path('records.db')
if database.exists():
    database.unlink()

conn = sqlite3.connect('records.db')
c = conn.cursor()

c.execute("CREATE TABLE authors (doi text, author text);")
c.execute("CREATE TABLE records (doi text, title text, published text, datacenter text);")

for json_file in json_files:
    data = json.loads(json_file.read_text())

    doi = 'https://doi.org/' + data['attributes']['doi']
    authors = data['attributes']['author']

    for author in authors:
        if author.get('literal'):
            author_name = author['literal']
        else:
            author_name = author['given'] + ' ' + author['family']
        authors_new_row = [doi, author_name]
        c.execute("INSERT INTO authors VALUES (?, ?)", authors_new_row)

    title = data['attributes']['title']
    published = data['attributes']['published']
    datacenter = str(data['relationships']['data-center']['data']['id'])
    records_new_row = [doi, title, published, datacenter]
    c.execute("INSERT INTO records VALUES (?, ?, ?, ?)", records_new_row)

conn.commit()

authors_results = c.execute("SELECT * FROM authors;")
authors_headers = [r[0] for r in authors_results.description]
authors_data = authors_results.fetchall()

with open('authors.csv', 'w', newline='', encoding='utf-8') as fout:
    csv_out = csv.writer(fout)
    csv_out.writerow(authors_headers)
    csv_out.writerows(authors_data)

bibinfo_results = c.execute("SELECT * FROM records;")
bibinfo_headers = [r[0] for r in bibinfo_results.description]
bibinfo_data = bibinfo_results.fetchall()

with open('bibinfo.csv', 'w', newline='', encoding='utf-8') as fout:
    csv_out = csv.writer(fout)
    csv_out.writerow(bibinfo_headers)
    csv_out.writerows(bibinfo_data)

datacenters_results = c.execute("SELECT DISTINCT authors.doi, datacenter, group_concat(author, '|') AS authors \
FROM authors JOIN records WHERE authors.doi = records.doi GROUP BY authors.doi;")
datacenters_headers = [r[0] for r in datacenters_results.description]
datacenters_data = datacenters_results.fetchall()

with open('datacenters.csv', 'w', newline='', encoding='utf-8') as fout:
    csv_out = csv.writer(fout)
    csv_out.writerow(datacenters_headers)
    csv_out.writerows(datacenters_data)

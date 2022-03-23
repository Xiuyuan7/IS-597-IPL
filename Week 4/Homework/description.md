I firstly use `shutil.unpack_archive('records.zip')` to unzip the records. Then I use `pathlib` module to get the list of paths of all json files. Then I check the existence of `records.db` database. If it exists, it will be deleted. Then I use `sqlite3` module to connect to the database and create a cursor. Then I use the cursor to create `authors` and `records` tables. Then I loop over the list of paths of all json files. For each iteration, I use `json.loads(json_file.read_text())` to get the data of the file and extract all information needed. Then I loop over the list of authors to get a record for each author. Then I use the cursor to insert the record to the two tables of the database. Then I commit the changes into the database. Then I use the cursor to get results from the database and separate headers and data from results. Then I write headers and data to the three csv files with `with open` statement.

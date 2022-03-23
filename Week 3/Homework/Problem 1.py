import pathlib
import json

target = pathlib.Path('data_for_profile_testing')

dictionary = {'files': [], 'directories': [], 'others': []}

results = list(target.glob('*'))

for subp in results:
    if subp.is_file():
        subp = str(subp.absolute())
        dictionary['files'].append(subp)
    elif subp.is_dir():
        subp = str(subp.absolute())
        dictionary['directories'].append(subp)
    else:
        subp = str(subp.absolute())
        dictionary['others'].append(subp)

with open(pathlib.Path('pathsfound.json'), 'w') as jout:
    json.dump(dictionary, jout, indent=4)

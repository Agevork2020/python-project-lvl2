import json
import yaml

source = 'gendiff/files/1.json'
def read(source):
    format = source.split('.')[1]
    if format == 'yаml':
        source = yaml.load(open(source))
    elif format == 'json':
        source = json.load(open(source))
    return source

a = [0, 2, 4, 6]
b = [1, 3, 4, 5]
print(list(set(a) - set(b)))

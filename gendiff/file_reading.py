import json
import yaml


def read(source):
    format = source.split('.')[1]
    if format == 'yаml':
        source = yaml.load(open(source))
    if format == 'json':
        source = json.load(open(source))
    return source

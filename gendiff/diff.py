import json
import yaml
from gendiff.format import stylish, plain


def read(source):
    format = source.split('.')[1]
    if format == 'yаml':
        source = yaml.load(open(source))
    if format == 'json':
        source = json.load(open(source))
    return source


def diff(source1, source2):
    result = {}
    stable = sorted(list(set(source1.keys()) & set(source2.keys())))
    added = sorted(list(set(source2.keys()) - set(source1.keys())))
    removed = sorted(list(set(source1.keys()) - set(source2.keys())))
    for i in stable:
        if type(source2[i]) != dict:
            if source1[i] == source2[i]:
                result[i] = {'status': 'unchanged', 'current_value': source2[i]}
            else:
                result[i] = {'status': 'changed', 'current_value': source2[i], 'old_value': source1[i]}
        else:
            result[i] = {'status': 'nested', 'diff': diff(source1[i], source2[i])}         
    for i in added:
        result[i] = {'status': 'added', 'current_value': source2[i]}
    for i in removed:
        result[i] = {'status': 'removed', 'old_value': source1[i]} 
    return result


def render_diff(source1, source2, format):
    file1 = read(source1)
    file2 = read(source2)
    if format == 'stylish':
        result = stylish(diff(file1, file2))
    elif format == 'plain':
        result = plain(diff(file1, file2))
    return result

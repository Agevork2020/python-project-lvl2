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
    unchanged = list(set(source1.keys()) & set(source2.keys()))
    added = list(set(source2.keys()) - set(source1.keys()))
    removed = list(set(source1.keys()) - set(source2.keys()))
    for key in unchanged:
        if type(source1[key]) == dict and type(source2[key]) == dict:
            result[key] = {'status': 'unchanged', 'dict':'true', 'diff': diff(source1[key], source2[key])}
        elif type(source1[key]) != dict and type(source2[key]) != dict:
            if source2[key] != source1[key]:
                result[key] = {'status': 'changed', 'dict':'false', 'current_value': source2[key], 'old_value': source1[key]}
            else: 
                result[key] = {'status': 'unchanged', 'dict':'false', 'current_value': source2[key], 'old_value': source1[key]}
        elif type(source2[key]) != dict and type(source1[key]) == dict:
            result[key] = {'status': 'changed_on_str', 'dict':'true', 'current_value': source2[key], 'diff': diff(source1[key], source1[key])}
        else:
            result[key] = {'status': 'changed_on_dict', 'dict':'true', 'diff': diff(source2[key], source2[key]), 'old_value': source1[key]}
    for key in added:
        if type(source2[key]) != dict:
            result[key] = {'status': 'added', 'dict':'false', 'current_value': source2[key], 'old_value': source2[key]}
        else:
            result[key] = {'status': 'added', 'dict':'true', 'diff': diff(source2[key], source2[key])}
    for key in removed:
        if type(source1[key]) != dict:
            result[key] = {'status': 'removed', 'dict':'false', 'current_value': source1[key], 'old_value': source1[key]}
        else:
            result[key] = {'status': 'removed', 'dict':'true', 'diff': diff(source1[key], source1[key])}       
    return result


def render_diff(source1, source2, format):
    file1 = read(source1)
    file2 = read(source2)
    if format == 'stylish':
        result = stylish(diff(file1, file2))
    elif format == 'plain':
        result = plain(diff(file1, file2))
    return result

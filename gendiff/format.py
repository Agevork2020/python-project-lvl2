import json


def plain(dict, prefix=''):
    result = ""
    for key, value in sorted(dict.items()):
        input = 'Property ' + f"'{prefix}.{key}'"
        if value['dict'] is False:
            if value['status'] == 'unchanged':
                continue
            elif value['status'] == 'added':
                s = input + ' was added with value: ' +\
                    f"'{str(value['current_value'])}'" + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'removed':
                s = input + ' was removed ' + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'changed':
                s = input + ' was updated. From ' +\
                    f"'{str(value['old_value'])}'" + ' to ' +\
                    f"'{str(value['current_value'])}'" + '\n'
                result = result + s[:10] + s[11:]
        elif value['dict'] is True:
            if value['status'] == 'unchanged':
                result = result + plain(value['diff'], f"{prefix}.{key}")
            elif value['status'] == 'added':
                s = input + ' was added with value: [complex value] ' + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'removed':
                s = input + ' was removed ' + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'changed_on_str':
                s = input + ' was updated. From [complex value] to ' +\
                    f"'{str(value['current_value'])}'" + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'changed_on_dict':
                s = input + ' was updated. From ' +\
                    f"'{str(value['old_value'])}'" +\
                    ' to [complex value]' + '\n'
                result = result + s[:10] + s[11:]
    return result


def stylish(dict, depth=0):
    result = '{\n'
    for key, value in sorted(dict.items()):
        if value['dict'] is False:
            if value['status'] == 'unchanged':
                result = result + depth * '    ' + '    ' + key + ': ' +\
                    str(value['current_value']) + '\n'
            elif value['status'] == 'added':
                result = result + depth * '    ' + '  + ' + key + ': ' +\
                    str(value['current_value']) + '\n'
            elif value['status'] == 'removed':
                result = result + depth * '    ' + '  - ' + key + ': ' +\
                    str(value['old_value']) + '\n'
            elif value['status'] == 'changed':
                result = result + depth * '    ' + '  - ' + key + ': ' +\
                    str(value['old_value']) + '\n'
                result = result + depth * '    ' + '  + ' + key + ': ' +\
                    str(value['current_value']) + '\n'
        elif value['dict'] is True:
            if value['status'] == 'unchanged':
                result = result + depth * '    ' + '    ' + key + ': ' +\
                    stylish(value['diff'], depth + 1) + '\n'
            elif value['status'] == 'added':
                result = result + depth * '    ' + '  + ' + key + ': ' +\
                    stylish(value['diff'], depth + 1) + '\n'
            elif value['status'] == 'removed':
                result = result + depth * '    ' + '  - ' + key + ': ' +\
                    stylish(value['diff'], depth + 1) + '\n'
            elif value['status'] == 'changed_on_str':
                result = result + depth * '    ' + '  - ' + key + ': ' +\
                    stylish(value['diff'], depth + 1) + '\n'
                result = result + depth * '    ' + '  + ' + key + ': ' +\
                    str(value['current_value']) + '\n'
            elif value['status'] == 'changed_on_dict':
                result = result + depth * '    ' + '  + ' + key + ': ' +\
                    stylish(value['diff'], depth + 1) + '\n'
                result = result + depth * '    ' + '  - ' + key + ': ' +\
                    str(value['old_value']) + '\n'
    result = result + depth * '    ' + '}'
    return result


def json_format(dict):
    return json.dumps(dict, indent=2)

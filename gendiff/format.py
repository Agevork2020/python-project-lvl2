

def plain(dict):
    result = ""
    for key, value in sorted(dict.items()):
        if value['dict'] == 'false':
            if value['status'] == 'unchanged':
                continue
            elif value['status'] == 'added':
                result = result + 'Property' + f'{prefix}.{path}' + 'was added with value:' + str(value['current_value']) + '\n'
            elif value['status'] == 'removed':
                result = result + 'Property' + f'{prefix}.{path}' + 'was removed' + '\n'
            elif value['status'] == 'changed':
                result = result + 'Property' + f'{prefix}.{path}' + 'was updated. From' + str(value['old_value']) + 'to' + str(value['current_value']) + '\n'
        elif value['dict'] == 'true':
            if value['status'] == 'unchanged':
                result = plain(value['diff'])
            elif value['status'] == 'added':
                result = result + 'Property' + f'{prefix}.{path}' + 'was added with value: [complex value]' + '\n'
            elif value['status'] == 'removed':
                result = result + 'Property' + f'{prefix}.{path}' + 'was removed' + '\n'
            elif value['status'] == 'changed_on_str':
                result = result + 'Property' + f'{prefix}.{path}' + 'was updated. From [complex value] to' + str(value['current_value']) + '\n'
            elif value['status'] == 'changed_on_dict':
                result + 'Property' + f'{prefix}.{path}' + 'was updated. From' + str(value['old_value']) + 'to [complex value]' + '\n'       
    result = result + '}'
    return result


def stylish(dict):
    result = '{ \n'
    for key, value in sorted(dict.items()):
        if value['dict'] == 'false':
            if value['status'] == 'unchanged':
                result = result + '    ' + key + ': ' + str(value['current_value']) + '\n'
            elif value['status'] == 'added':
                result = result + '  + ' + key + ': ' + str(value['current_value']) + '\n'
            elif value['status'] == 'removed':
                result = result + '  - ' + key + ': ' + str(value['current_value']) + '\n'
            elif value['status'] == 'changed':
                result = result + '  + ' + key + ': ' + str(value['current_value']) + '\n'
                result = result + '  - ' + key + ': ' + str(value['old_value']) + '\n'
        elif value['dict'] == 'true':
            if value['status'] == 'unchanged':
                result = result + '    ' + key + ': ' + stylish(value['diff']) + '\n'
            elif value['status'] == 'added':
                result = result + '  + ' + key + ': ' + stylish(value['diff']) + '\n'
            elif value['status'] == 'removed':
                result = result + '  - ' + key + ': ' + stylish(value['diff']) + '\n'
            elif value['status'] == 'changed_on_str':
                result = result + '  + ' + key + ': ' + str(value['current_value']) + '\n'
                result = result + '  - ' + key + ': ' + stylish(value['diff']) + '\n'
            elif value['status'] == 'changed_on_dict':
                result = result + '  - ' + key + ': ' + str(value['old_value']) + '\n'
                result = result + '  + ' + key + ': ' + stylish(value['diff']) + '\n'       
    result = result + '}'
    return result

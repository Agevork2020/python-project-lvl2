

def plain(dict):
    result = ""
    for key, value in dict.items():
        if value['status'] == 'unchanged':
            continue
        if value['status'] == 'changed':
            result = result + 'Property {1} was updated. From {2} to {3}'.format(key, value['old_value'], value['current_value']) + '\n'
        if value['status'] == 'added':
            result = result + 'Property {1} was added with value: {2}'.format(key, value['current_value']) + '\n'
        if value['status'] == 'removed':
            result = result + 'Property {1} was removed'.format(key) + '\n'
        elif value['status'] == 'nested':
            result = result + plain(value['diff']) + '\n'
    return result


def stylish(dict):
    result = '{ \n'
    for key, value in dict.items():
        if value['status'] == 'unchanged':
            result = result + '    ' + key + ': ' + str(value['current_value']) + '\n'
        if value['status'] == 'changed':
            result = result + '  + ' + key + ': ' + str(value['current_value']) + '\n'
            result = result + '  - ' + key + ': ' + str(value['old_value']) + '\n'
        if value['status'] == 'added':
            result = result + '  + ' + key + ': ' + str(value['current_value']) + '\n'
        if value['status'] == 'removed':
            result = result + '  - ' + key + ': ' + str(value['old_value']) + '\n'
        elif value['status'] == 'nested':
            result = result + '    ' + key + ': ' + stylish(value['diff']) + '\n'
    result = result + '}'
    return result

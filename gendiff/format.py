

def plain(dict, prefix=''):
    result = ""
    for key, value in sorted(dict.items()):
        if value['dict'] == 'false':
            if value['status'] == 'unchanged':
                continue
            elif value['status'] == 'added':
                s = 'Property ' + f"'{prefix}.{key}'" + ' was added with value: ' + f"'{str(value['current_value'])}'" + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'removed':
                s = 'Property ' + f"'{prefix}.{key}'" +  ' was removed ' + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'changed':
                s = 'Property ' + f"'{prefix}.{key}'" + ' was updated. From ' + f"'{str(value['old_value'])}'" + ' to ' + f"'{str(value['current_value'])}'" + '\n'
                result = result + s[:10] + s[11:]
        elif value['dict'] == 'true':
            if value['status'] == 'unchanged':
                result = result + plain(value['diff'], f"{prefix}.{key}")
            elif value['status'] == 'added':
                s = 'Property ' + f"'{prefix}.{key}'" + ' was added with value: [complex value] ' + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'removed':
                s = 'Property ' + f"'{prefix}.{key}'" + ' was removed ' + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'changed_on_str':
                s = 'Property ' + f"'{prefix}.{key}'" + ' was updated. From [complex value] to ' + f"'{str(value['current_value'])}'" + '\n'
                result = result + s[:10] + s[11:]
            elif value['status'] == 'changed_on_dict':
                s = 'Property ' + f"'{prefix}.{key}'" + ' was updated. From ' + f"'{str(value['old_value'])}'" + ' to [complex value]' + '\n'  
                result = result + s[:10] + s[11:]     
    return result


def stylish(dict, depth=0):
    result = '{ \n'
    for key, value in sorted(dict.items()):
        if value['dict'] == 'false':
            if value['status'] == 'unchanged':
                result = result + depth*'   ' + '    ' + key + ': ' + str(value['current_value']) + '\n'
            elif value['status'] == 'added':
                result = result + depth*'   ' + '  + ' + key + ': ' + str(value['current_value']) + '\n'
            elif value['status'] == 'removed':
                result = result + depth*'   ' + '  - ' + key + ': ' + str(value['current_value']) + '\n'
            elif value['status'] == 'changed':
                result = result + depth*'   ' + '  + ' + key + ': ' + str(value['current_value']) + '\n'
                result = result + depth*'   ' + '  - ' + key + ': ' + str(value['old_value']) + '\n'
        elif value['dict'] == 'true':
            if value['status'] == 'unchanged':
                result = result + depth*'   ' + '    ' + key + ': ' + stylish(value['diff'], depth+1) + '\n'
            elif value['status'] == 'added':
                result = result + depth*'   ' + '  + ' + key + ': ' + stylish(value['diff'], depth+1) + '\n'
            elif value['status'] == 'removed':
                result = result + depth*'   ' + '  - ' + key + ': ' + stylish(value['diff'], depth+1) + '\n'
            elif value['status'] == 'changed_on_str':
                result = result + depth*'   ' + '  + ' + key + ': ' + str(value['current_value']) + '\n'
                result = result + depth*'   ' + '  - ' + key + ': ' + stylish(value['diff'], depth+1) + '\n'
            elif value['status'] == 'changed_on_dict':
                result = result + depth*'   ' + '  - ' + key + ': ' + str(value['old_value']) + '\n'
                result = result + depth*'   ' + '  + ' + key + ': ' + stylish(value['diff'], depth+1) + '\n'    
    result = result +  depth*'    ' + '}'
    return result


def json_format(dict):
    return json.dumps(dict, indent=2)
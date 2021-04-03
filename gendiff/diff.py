

def diff(source1, source2):
    result = {}
    for key in sorted(source1.keys() & source2.keys()):
        if type(source1[key]) == dict and type(source2[key]) == dict:
            result[key] = {
                'status': 'unchanged', 'dict': True, 'diff': diff(
                    source1[key], source2[key])}
        elif type(source1[key]) != dict and type(source2[key]) != dict:
            if source2[key] != source1[key]:
                result[key] = {
                    'status': 'changed', 'dict': False,
                    'current_value': source2[key], 'old_value': source1[key]}
            else:
                result[key] = {
                    'status': 'unchanged', 'dict': False,
                    'current_value': source2[key], 'old_value': source1[key]}
        elif type(source2[key]) != dict and type(source1[key]) == dict:
            result[key] = {
                'status': 'changed_on_str', 'dict': True,
                'current_value': source2[key],
                'diff': diff(source1[key], source1[key])}
        else:
            result[key] = {
                'status': 'changed_on_dict', 'dict': True,
                'diff': diff(source2[key], source2[key]),
                'old_value': source1[key]}
    for key in sorted(source2.keys() - source1.keys()):
        if type(source2[key]) != dict:
            result[key] = {
                'status': 'added', 'dict': False,
                'current_value': source2[key]}
        else:
            result[key] = {
                'status': 'added', 'dict': True,
                'diff': diff(source2[key], source2[key])}
    for key in sorted(source1.keys() - source2.keys()):
        if type(source1[key]) != dict:
            result[key] = {
                'status': 'removed', 'dict': False,
                'old_value': source1[key]}
        else:
            result[key] = {
                'status': 'removed', 'dict': True,
                'diff': diff(source1[key], source1[key])}
    return result

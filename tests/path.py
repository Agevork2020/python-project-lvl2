

def sniff_glue(file, *folders):
    path = f'{file}'
    for folder in folders:
        path = f'{folder}/' + path
    path = f"'{path}'"
    return path

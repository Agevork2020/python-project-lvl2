from gendiff.format import stylish, plain, json_format
from gendiff.file_reading import read
from gendiff.diff import diff


def render_diff(source1, source2, format):
    file1 = read(source1)
    file2 = read(source2)
    if format == 'stylish':
        result = stylish(diff(file1, file2))
    elif format == 'plain':
        result = plain(diff(file1, file2))
    elif format == 'json_format':
        result = json_format(diff(file1, file2))
    return result

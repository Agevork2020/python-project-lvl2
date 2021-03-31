from gendiff import generate_diff
from fixtures.test_results import result, children_structure


def test_diff_json():
    assert generate_diff.generate_diff('gendiff/files/1.json', 'gendiff/files/2.json') == result


def test_diff_yaml():
    assert generate_diff.generate_diff('gendiff/files/1.yaml', 'gendiff/files/2.yaml') == result


def test_diff_child_json():
    assert generate_diff.generate_diff('gendiff/files/11.json', 'gendiff/files/12.json') == children_structure


def test_diff_child_yaml():
    assert generate_diff.generate_diff('gendiff/files/11.yaml', 'gendiff/files/12.yaml') == children_structure

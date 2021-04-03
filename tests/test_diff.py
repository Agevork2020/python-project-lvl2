from gendiff.generate_diff import render_diff
from fixtures.test_results import result, stylish_structure, plain_structure
from path import sniff_glue


plain_1_json = sniff_glue(
    '1_plain.json', 'gendiff', 'tests', 'fixtures', 'files')
plain_2_json = sniff_glue(
    '2_plain.json', 'gendiff', 'tests', 'fixtures', 'files')
plain_1_yaml = sniff_glue(
    '1_plain.yaml', 'gendiff', 'tests', 'fixtures', 'files')
plain_2_yaml = sniff_glue(
    '2_plain.yaml', 'gendiff', 'tests', 'fixtures', 'files')
nested_1_json = sniff_glue(
    '1_nested.json', 'gendiff', 'tests', 'fixtures', 'files')
nested_2_json = sniff_glue(
    '2_nested.json', 'gendiff', 'tests', 'fixtures', 'files')
nested_1_yaml = sniff_glue(
    '1_nested.yaml', 'gendiff', 'tests', 'fixtures', 'files')
nested_2_yaml = sniff_glue(
    '2_nested.yaml', 'gendiff', 'tests', 'fixtures', 'files')


def test_diff_json():
    assert render_diff(plain_1_json, plain_2_json) == result


def test_diff_yaml():
    assert render_diff(plain_1_yaml, plain_2_yaml) == result


def test_diff_stylish_json():
    assert render_diff(
        nested_1_json, nested_2_json) == stylish_structure


def test_diff_stylish_yaml():
    assert render_diff(
        nested_1_yaml, nested_2_yaml) == stylish_structure


def test_diff_plain_json():
    assert render_diff(
        nested_1_json, nested_2_json) == plain_structure


def test_diff_plain_yaml():
    assert render_diff(
        nested_1_yaml, nested_2_yaml) == plain_structure

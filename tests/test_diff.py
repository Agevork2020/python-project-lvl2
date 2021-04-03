from gendiff.generate_diff import render_diff
from fixtures.test_results import (
    simple, stylish_structure, plain_structure, json_structure)
from path import sniff_glue


plain_1_json = sniff_glue(
    '1_plain.json', 'files', 'fixtures', 'tests')
plain_2_json = sniff_glue(
    '2_plain.json', 'files', 'fixtures', 'tests')
plain_1_yaml = sniff_glue(
    '1_plain.yaml', 'files', 'fixtures', 'tests')
plain_2_yaml = sniff_glue(
    '2_plain.yaml', 'files', 'fixtures', 'tests')
nested_1_json = sniff_glue(
    '1_nested.json', 'files', 'fixtures', 'tests')
nested_2_json = sniff_glue(
    '2_nested.json', 'files', 'fixtures', 'tests')
nested_1_yaml = sniff_glue(
    '1_nested.yaml', 'files', 'fixtures', 'tests')
nested_2_yaml = sniff_glue(
    '2_nested.yaml', 'files', 'fixtures', 'tests')


def test_diff_json():
    assert render_diff('tests/fixtures/files/1_plain.json', 'tests/fixtures/files/2_plain.json', 'stylish') == simple

def test_diff_json():
    assert render_diff(plain_1_json, plain_2_json, 'stylish') == simple


def test_diff_yaml():
    assert render_diff(plain_1_yaml, plain_2_yaml, 'plain') == simple


def test_diff_stylish_json():
    assert render_diff(
        nested_1_json, nested_2_json, 'stylish') == stylish_structure


def test_diff_stylish_yaml():
    assert render_diff(
        nested_1_yaml, nested_2_yaml, 'stylish') == stylish_structure


def test_diff_plain_json():
    assert render_diff(
        nested_1_json, nested_2_json, 'plain') == plain_structure


def test_diff_plain_yaml():
    assert render_diff(
        nested_1_yaml, nested_2_yaml, 'plain') == plain_structure


def test_diff_json_json():
    assert render_diff(
        nested_1_json, nested_2_json, 'json_format') == json_structure


def test_diff_json_yaml():
    assert render_diff(
        nested_1_yaml, nested_2_yaml, 'json_format') == json_structure
simple = """\
{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""


stylish_structure = """\
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

plain_structure = """\
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""
json_structure = """\
{
  "group1": {
    "status": "unchanged",
    "dict": "true",
    "diff": {
      "nest": {
        "status": "changed_on_str",
        "dict": "true",
        "current_value": "str",
        "diff": {
          "key": {
            "status": "unchanged",
            "dict": "false",
            "current_value": "value",
            "old_value": "value"
          }
        }
      },
      "baz": {
        "status": "changed",
        "dict": "false",
        "current_value": "bars",
        "old_value": "bas"
      },
      "foo": {
        "status": "unchanged",
        "dict": "false",
        "current_value": "bar",
        "old_value": "bar"
      }
    }
  },
  "common": {
    "status": "unchanged",
    "dict": "true",
    "diff": {
      "setting1": {
        "status": "unchanged",
        "dict": "false",
        "current_value": "Value 1",
        "old_value": "Value 1"
      },
      "setting3": {
        "status": "changed",
        "dict": "false",
        "current_value": "null",
        "old_value": "true"
      },
      "setting6": {
        "status": "unchanged",
        "dict": "true",
        "diff": {
          "doge": {
            "status": "unchanged",
            "dict": "true",
            "diff": {
              "wow": {
                "status": "changed",
                "dict": "false",
                "current_value": "so much",
                "old_value": ""
              }
            }
          },
          "key": {
            "status": "unchanged",
            "dict": "false",
            "current_value": "value",
            "old_value": "value"
          },
          "ops": {
            "status": "added",
            "dict": "false",
            "current_value": "vops",
            "old_value": "vops"
          }
        }
      },
      "setting5": {
        "status": "added",
        "dict": "true",
        "diff": {
          "key5": {
            "status": "unchanged",
            "dict": "false",
            "current_value": "value5",
            "old_value": "value5"
          }
        }
      },
      "setting4": {
        "status": "added",
        "dict": "false",
        "current_value": "blah blah",
        "old_value": "blah blah"
      },
      "follow": {
        "status": "added",
        "dict": "false",
        "current_value": "false",
        "old_value": "false"
      },
      "setting2": {
        "status": "removed",
        "dict": "false",
        "current_value": 200,
        "old_value": 200
      }
    }
  },
  "group3": {
    "status": "added",
    "dict": "true",
    "diff": {
      "deep": {
        "status": "unchanged",
        "dict": "true",
        "diff": {
          "id": {
            "status": "unchanged",
            "dict": "true",
            "diff": {
              "number": {
                "status": "unchanged",
                "dict": "false",
                "current_value": 45,
                "old_value": 45
              }
            }
          }
        }
      },
      "fee": {
        "status": "unchanged",
        "dict": "false",
        "current_value": 100500,
        "old_value": 100500
      }
    }
  },
  "group2": {
    "status": "removed",
    "dict": "true",
    "diff": {
      "abc": {
        "status": "unchanged",
        "dict": "false",
        "current_value": 12345,
        "old_value": 12345
      },
      "deep": {
        "status": "unchanged",
        "dict": "true",
        "diff": {
          "id": {
            "status": "unchanged",
            "dict": "false",
            "current_value": 45,
            "old_value": 45
          }
        }
      }
    }
  }
}"""

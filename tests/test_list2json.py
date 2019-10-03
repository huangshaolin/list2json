#!/usr/bin/env python3

import json
import subprocess
import unittest

import list2json


class TestIndentedLinesToDict(unittest.TestCase):

    def test_main(self):
        list2json_path = list2json.__file__
        result = subprocess.run(
            'python3 %s tests/test.md tests/test.json.tmp --indent="---"' % list2json_path, shell=True, check=True)
        self.assertEqual(result.returncode, 0)
        with open('tests/test.json.tmp', 'r') as f1:
            with open('tests/test.json', 'r') as f2:
                json1 = json.load(f1)
                json2 = json.load(f2)
                self.assertEqual(json1, json2)


if __name__ == '__main__':
    unittest.main()

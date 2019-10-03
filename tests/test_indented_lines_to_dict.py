#!/usr/bin/env python3

import unittest

import indented_lines_to_dict


class TestIndentedLinesToDict(unittest.TestCase):

    def test_get_indent_count(self):
        indented_lines = [
            ('\t' * 3 + 'abc hello  ', '\t', 3),
            ('   ' * 4 + 'abc hello ', '   ', 4),
            ('    ' * 7 + 'abc hello', '    ', 7)
        ]
        for line in indented_lines:
            line_str = line[0]
            indentation = line[1]
            indent_count = line[2]
            self.assertEqual(
                indent_count, indented_lines_to_dict.get_indent_count(line_str, indentation))

    def test_create_node(self):
        data_list = [-2, 0, 1, 13, '', 'abc', {},
                     {'name': 'mike'}, [], [1, 2, 3], (), ('a', 'b')]
        for data in data_list:
            node = indented_lines_to_dict.create_node(data)
            self.assertEqual(node, {"data": data, "children": []})

    def test_remove_indent(self):
        indented_lines = [
            ('\t' * 3 + 'abc hello  ', '\t', 'abc hello  '),
            ('   ' * 4 + 'abc hello ', '   ', 'abc hello '),
            ('    ' * 7 + 'abc hello', '    ', 'abc hello')
        ]
        for line in indented_lines:
            line_str = line[0]
            indentation = line[1]
            result = line[2]
            self.assertEqual(
                result, indented_lines_to_dict.remove_indent(line_str, indentation))

    def test_indented_lines_to_dict(self):
        indented_lines_list = [
            ('', {'data': '', 'children': [{'data': '', 'children': []}]}),
            ('a', {'data': '', 'children': [{'data': 'a', 'children': []}]}),
            ('a\n\ta1\n\ta2\n\t\ta21',
             {'data': '', 'children': [
                 {'data': 'a', 'children': [
                     {'data': 'a1', 'children': []},
                     {'data': 'a2', 'children': [
                         {'data': 'a21', 'children': []}
                     ]}
                 ]}
             ]})
        ]
        for lines in indented_lines_list:
            indented_lines = lines[0].split('\n')
            result = lines[1]
            self.assertEqual(
                result, indented_lines_to_dict.indented_lines_to_dict(indented_lines, '\t'))


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3


def get_indent_count(s, indent_str):
    count = 0
    indent_len = len(indent_str)
    while s[count*indent_len:(count+1)*indent_len] == indent_str:
        count += 1
    return count


def create_node(data):
    node = {"data": data, "children": []}
    return node


def remove_indent(s, indent_str):
    return s[get_indent_count(s, indent_str)*len(indent_str):]


def indented_lines_to_dict(lines, indent_str):
    root = create_node("")
    newest_nodes_by_depth = [root]
    for s in lines:
        line_node = create_node(remove_indent(s, indent_str))
        line_depth = get_indent_count(s, indent_str) + 1
        if line_depth >= len(newest_nodes_by_depth):
            line_depth = len(newest_nodes_by_depth)
            newest_nodes_by_depth.append(line_node)
        parent = newest_nodes_by_depth[line_depth-1]
        parent["children"].append(line_node)
        newest_nodes_by_depth[line_depth] = line_node
    return root

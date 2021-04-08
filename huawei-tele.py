#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lWX636554'

from lxml import etree

xml_fie = r"C:\Users\gwx5320012\Desktop\transfer\acl_schema_tailor.xml"
if __name__ == "__main__":

    with open(xml_fie, "r") as file:
        xml_str = file.read()
    schema_root = etree.fromstring(xml_str.encode('utf-8')).getroottree()
    file_nodes = schema_root.xpath("/schema/white_list/file")
    if file_nodes:
        for file_node in file_nodes:
            if file_node.attrib and file_node.attrib.get("name"):
                if file_node.attrib.get("multitailor") == 'true':
                    continue
                name_value = file_node.attrib["name"]
                cut_nodes = schema_root.xpath("/schema/cut[@schemaFile='" + name_value + "']")
                path_set = set()
                for cut_node in cut_nodes:
                    if cut_node.attrib and cut_node.attrib.get("path"):
                        path_set.add(cut_node.attrib.get("path"))
                if len(path_set) > 1:
                    file_node.set('multitailor', 'true')
    print(etree.tostring(schema_root))
    result = etree.tostring(schema_root, pretty_print=True)
    a = str(result,encoding='utf-8')
    with open(xml_fie, "w") as file:
        file.write(a)

#!/usr/bin/env python3
""" Cette commande effectue de la validation XML avec éventuellement un schéma XML"""

import sys
from lxml import etree
import argparse

def main():
    """Programme principal"""
    parser = argparse.ArgumentParser(
        description='Effectue de la validation XML avec éventuellement un schéma XML'
    )
    parser.add_argument('-x', dest="xsd", nargs="?", metavar='xsdfile', help='Le schéma XML')
    parser.add_argument('xmlpaths_list', metavar='xmlfile', nargs='+', help='Fichier xml à valider')
    args = parser.parse_args()

    if args.xsd is None:
        schema = None
    else:
        try:
            with open(args.xsd) as schema_file:
                schema = etree.XMLSchema(etree.XML(schema_file.read()))
        except (FileNotFoundError, PermissionError) as error:
            print("Impossible de lire le fichier xsd '{}' : ".format(args.xsd), error)
            sys.exit(1)

    parser = etree.XMLParser(schema=schema)

    return_code = 0
    for xml_path in args.xmlpaths_list:
        try:
            with open(xml_path) as xml_file:
                xml_str = xml_file.read()
        except (FileNotFoundError, PermissionError) as error:
            print("Impossible de lire le fichier xml '{}' : ".format(xml_path), error)
            return_code = 1
            continue

        try:
            etree.fromstring(xml_str, parser)
        except etree.XMLSyntaxError as error:
            print("Fichier xml '{}' invalide : ".format(xml_path), error)
        else:
            print("Fichier xml '{}' valide".format(xml_path))

    sys.exit(return_code)

if __name__ == "__main__":
    main()

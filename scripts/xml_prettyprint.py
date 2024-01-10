#!/usr/bin/env python3
"""Commande permettant d'Afficher le xml de façon à ce qu'il soit lisible"""

import sys
import xml.dom.minidom as minidom
import argparse


def main():
    """Programme principal"""
    parser = argparse.ArgumentParser(
        description='Affiche le xml de façon à ce qu\'il soit lisible'
    )
    parser.add_argument(
        'xmlpaths_list',
        metavar='xmlfile',
        nargs='+',
        help='Fichier xml à transformer'
    )

    args = parser.parse_args()

    return_code = 0

    for xmlpath in args.xmlpaths_list:
        try:
            xml = minidom.parse(xmlpath)
        except (FileNotFoundError, PermissionError) as error:
            print("Impossible de lire le fichier xml '{}' : ".format(xmlpath), error)
            return_code = 1
            continue
        print(xml.toprettyxml())

    sys.exit(return_code)


if __name__ == "__main__":
    main()

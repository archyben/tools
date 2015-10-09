#!/usr/bin/env python3
"""
Cette commande permet de transformer un timestamp en date et inversement.
Elle peut aussi fournir le timestamp actuel
"""

import argparse
from datetime import datetime as dt

# Constantes
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def timestamp_to_date(timestamp):
    """Convertit un timestamp en date"""
    return dt.fromtimestamp(timestamp / 1000).strftime(DATE_FORMAT)

def date_to_timestamp(date):
    """Convertit une date au format timestamp"""
    return int(dt.strptime(date, DATE_FORMAT).timestamp() * 1000)

def get_now_timestamp():
    """Donne le timestamp actuel"""
    return int(dt.now().timestamp() * 1000)

def main():
    """Fonction principal"""
    parser = argparse.ArgumentParser(description='Gestion des timestamp')
    group = parser.add_mutually_exclusive_group()
    group.required = True
    group.add_argument(
        '-d',
        dest="date",
        metavar='date',
        help='Date au format {} à convertir'.format(DATE_FORMAT)
    )
    group.add_argument(
        '-t',
        dest="timestamp",
        metavar='timestamp',
        help='Timestamp à convertir',
        type=int
    )
    group.add_argument(
        '-n',
        dest="now",
        action="store_true",
        help='Donne le timestamp de ce moment'
    )
    args = parser.parse_args()

    # En fonction des arguments, appelle la bonne méthode
    if args.date is not None:
        print(date_to_timestamp(args.date))
    elif args.timestamp is not None:
        print(timestamp_to_date(args.timestamp))
    else:
        print(get_now_timestamp())

# Mise en place du parser d'argument
if __name__ == "__main__":
    main()

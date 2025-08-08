from sys import argv
from os import path
from types import *

import argparse
import logging
import json
import csv


def main():

    '''
    parser = argparse.ArgumentParser(
        description='Convert json file to csv'
    )

    parser.add_argument(
        '-i',
        '-test1.json',
        dest='json-1',
        default=None,
        required=True,
        help='test11.json'
    )
    parser.add_argument(
        '-o',
        '--output_file',
        dest='csv-1',
        default=None,
        required=True,
        help='test11.csv'
    )

    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    '''

    input_file = 'cdf1.json'
    output_file = 'cdf1.csv'


    json_data = []
    data = None
    write_header = True
    item_keys = []

    with open(input_file) as json_file:
        json_data = json_file.read()

    try:
        data = json.loads(json_data)
    except Exception as e:
        raise e
    
 
    with open(output_file, 'wb') as csv_file:
        writer = csv.writer(csv_file)

        for item in data:
            item_values = []
            for key in item:
                if write_header:
                    item_keys.append(key)

                value = item.get(key, '')
                if isinstance(value, StringTypes):
                    item_values.append(value.encode('utf-8'))
                else:
                    item_values.append(value)

            if write_header:
                writer.writerow(item_keys)
                write_header = False

            writer.writerow(item_values)

if __name__ == "__main__":
    main()


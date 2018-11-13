#!/usr/bin/env python
"""
Command line program for running the pagination

You do not need to edit this file for the programming exercise. All work can be
done in pagination.py.
"""

import argparse

from pagination import paginate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='path to the CSV input file')
    parser.add_argument(
        '--sort-by', help="name of column to sort by", required=True)
    parser.add_argument(
        '--page-size', type=int, help="number of records per page (minimum 1)",
        required=True
    )
    parser.add_argument(
        '--page-num', type=int, help="page number to show (minimum 1)",
        required=True
    )
    args = parser.parse_args()

    with open(args.file_path) as f:
        file_text = f.read()
    output_text = paginate(
        file_text,
        sort_by=args.sort_by,
        page_size=args.page_size,
        page_num=args.page_num
    )
    print(output_text)


if __name__ == "__main__":
    main()

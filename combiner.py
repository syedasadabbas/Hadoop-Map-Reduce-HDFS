#!/usr/bin/env python3

from itertools import groupby

# Student ID: 3309776

def parse_input(line):
    uid, title, genre, year, rating = line.strip().split('\t')
    return uid, (title, rating, year)

def format_output(data):
    title, rating, year = data
    appearance_count = len(rating)
    rating_str = ','.join([r[1] for r in rating])
    return f"{year}\t{title}\t{rating[0][0]}\t{'[' + '1,' * (appearance_count-1) + '1]' if appearance_count > 0 else '[]'}"

def main():    
    with open('mapout.txt', 'r') as f:
        lines = f.readlines()

    lines.sort(key=lambda x: x.strip().split('\t')[3], reverse=True)

    grouped_lines = groupby(lines, key=lambda x: x.strip().split('\t')[0])

    with open('comout.txt', 'w') as outfile:
        for uid, group in grouped_lines:
            title = ''
            rating = []
            year = ''

            for line in group:
                parsed_data = parse_input(line)
                title = parsed_data[1][0]
                rating.append(parsed_data[1][1:])
                year = parsed_data[1][2]

            output_line = format_output((title, rating, year))
            outfile.write(output_line + '\n')

if __name__ == "__main__":
    main()
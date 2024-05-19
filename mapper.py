#!/usr/bin/env python3
import sys

with open('years.txt', 'r') as f:
    years = set(f.read().split())

for line in sys.stdin:
    # print("Processing line:", line.strip())
    fields = line.strip().split('\t')
    if len(fields) != 5:
        # print("Invalid line:", line.strip())
        continue
    
    uid, title, genres, year, rating = fields
    # print("Fields:", uid, title, genres, year, rating)

    if year not in years:
        # print("Year not in the list of years:", year)
        continue

    for genre in genres.split('|'):
        key = f"{year}|{title}"
        value = f"{rating}|1"
        # print("Emitting key-value pair - Key:", key, ", Value:", value)
        # print(f"{key}\t{value}")

with open('r100.txt', 'r') as f, open('mapout.txt', 'w') as mapout:
    for line in f:
        # print("Processing r100 line:", line.strip())
        fields = line.strip().split('\t')
        if len(fields) != 5:
            # print("Invalid r100 line:", line.strip())
            continue
        
        uid, title, genres, year, rating = fields
        # print("Fields from r100:", uid, title, genres, year, rating)
        
        if year not in years:
            # print("Year not in the list of years:", year, "in r100.txt")
            continue

        for genre in genres.split('|'):

            key = f"{year}|{title}"
            value = f"{rating}|1"
            # print("Emitting key-value pair from r100 - Key:", key, ", Value:", value)
            # print(f"{key}\t{value}")
            mapout.write(f"{uid}\t{title}\t{genre}\t{year}\t{rating}\n")

from collections import defaultdict

def calculate_total(appearance_count):
    return sum(int(count) for count in appearance_count.strip('[]').split(','))

def parse_line(line):
    year, title, rating, appearance_count = line.strip().split('\t')
    return int(year), title, float(rating), calculate_total(appearance_count)

def write_results(results):
    with open('results.txt', 'w') as f:
        f.write("Year\tMovie_Title\tMovie_Rating\n")
        for year, movies in results.items():
            for movie in movies:
                f.write(f"{year}\t{movie[0]}\t{movie[1]}\n")

def main():
    min_votes = 10
    results = defaultdict(list)

    with open('comout.txt', 'r') as f:
        for line in f:
            year, title, rating, appearance_count = parse_line(line)
            if appearance_count >= min_votes:
                if not results[year] or rating > results[year][0][1]:
                    results[year] = [(title, rating)]
                elif rating == results[year][0][1]:
                    results[year].append((title, rating))
    write_results(results)

if __name__ == "__main__":
    main()
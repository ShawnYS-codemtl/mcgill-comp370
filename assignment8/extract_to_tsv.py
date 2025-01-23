import argparse
from pathlib import Path
import json
import random
import csv

def get_datafile_path(fname):
    return Path(__file__).parent / fname

def load_keywords(input_file):
    input_path = get_datafile_path(input_file)
    keywords_dict = json.load(open(input_path, "r"))
    return keywords_dict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--out_file", help="Output file")
    parser.add_argument("json_file", help="Path to output json file")
    parser.add_argument("num_posts_to_output", help="Limit number of posts", type=int)
    args = parser.parse_args()

    keywords_dict = load_keywords(args.json_file)
    post_list = keywords_dict["data"]["children"]
    random.shuffle(post_list)
    header = ["Name", "title", "coding"]
    count = 0

    with open(args.out_file, 'w', newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
        writer.writerow(header)

        for post in post_list:
            if count > args.num_posts_to_output:
                break
            name = post["data"]["name"]
            title = post["data"]["title"]
            writer.writerow([name, title, ''])
            count += 1

if __name__ == "__main__":
    main()
    

import argparse
import json
from pathlib import Path
import sys
sys.path.append('/Users/shawnyatsin/assignments/COMP370/hmk6/newscover')
from newsapi import fetch_latest_news
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k","--api_key", help="Name of show to fetch episodes for", required=True)
    parser.add_argument("-b","--lookback_days", help="nb of days to lookback")
    parser.add_argument("-i","--input_file", help="dictionary of keyword lists", required=True)
    parser.add_argument("-o","--output_dir", help="Path to output json file", required=True)
    args = parser.parse_args()

    if args.lookback_days:
        fetch_list_keywords(args.input_file, args.output_dir, args.api_key, args.lookback_days)

    else:
        fetch_list_keywords(args.input_file, args.output_dir, args.api_key)


def get_datafile_path(fname):
    return Path(__file__).parent / fname

def load_keywords(input_file):
    input_path = get_datafile_path(input_file)
    keywords_dict = json.load(open(input_path, "r"))
    return keywords_dict

def fetch_list_keywords(input_file, output_dir, api_key, lookback_days=0):
    keywords_dict = load_keywords(input_file)
    print(keywords_dict)

    for key in keywords_dict:
        search_str = '+OR+'.join(keywords_dict[key])
        print(search_str)
        news_data = fetch_latest_news(api_key, search_str,lookback_days=0)
        output_file = output_dir + "/" + key + ".json"
        with open(output_file, 'w') as f:
            json.dump(news_data, f, indent = 4)

if __name__ == "__main__":
    main()













    






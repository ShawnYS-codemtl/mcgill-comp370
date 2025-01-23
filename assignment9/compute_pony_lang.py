import csv
import argparse
import json
from pathlib import Path
import math
from operator import itemgetter

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("-c","--input_path", help="the input filepath")
        parser.add_argument("-n","--num_words", help="the number of words for each pony")
        args = parser.parse_args()

        compute_pony_words(args.input_path, args.num_words)

def get_datafile_path(fname):
    return Path(__file__).parent / fname

def load_keywords(input_file):
    input_path = get_datafile_path(input_file)
    keywords_dict = json.load(open(input_path, "r"))
    return keywords_dict

def compute_pony_words(input_file, num_words):
        word_count_dict = load_keywords(input_file)

        pony_lang_dict = {"Twilight Sparkle":{}, "Fluttershy":{}, "Pinkie Pie":{}, "Rarity":{}, "Rainbow Dash":{}, "Applejack":{}}

        for pony in word_count_dict:
              top_words = []
              for word in word_count_dict[pony]:
                    tf = word_count_dict[pony][word]
                    nb_ponies_that_use_word = 0
                    for pony2 in word_count_dict:
                          if word in word_count_dict[pony2]:
                                nb_ponies_that_use_word += 1
                                
                    idf = math.log(6/nb_ponies_that_use_word)
                    tf_idf = tf * idf
                    top_words.append((word,tf_idf))
              top_words = sorted(top_words, reverse=True, key=itemgetter(1))
              final_word_list_and_scores = top_words[:int(num_words)]
              final_word_list = []
              for tup in final_word_list_and_scores:
                    final_word_list.append(tup[0])
              pony_lang_dict[pony] = final_word_list
        
        print(pony_lang_dict)

if __name__ == "__main__":
    main()

            

                    


                    
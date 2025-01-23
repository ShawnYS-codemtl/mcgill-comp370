import csv
import argparse
import json

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("-o","--output_path", help="the output filepath")
        parser.add_argument("-d","--data_path", help="the data filepath")
        args = parser.parse_args()

        compile_word_counts(args.output_path, args.data_path)

def filter_function(pair):
    key, value = pair
    if value < 5:
        return False
    else:
        return True

def compile_word_counts(output_file, input_file):
    with open(input_file, "r", encoding="unicode_escape") as infile, open(output_file, "w", newline="") as outfile:
        reader = csv.reader(infile)

        #ponies = ["Twilight Sparkle", "Fluttershy", "Pinkie Pie", "Rarity", "Rainbow Dash", "Applejack"]
        word_dictionary = {"Twilight Sparkle":{}, "Fluttershy":{}, "Pinkie Pie":{}, "Rarity":{}, "Rainbow Dash":{}, "Applejack":{}}

        punctuation_chars = ["(",")","[","]","-",",",".","?","!",":",";","#","&"]
        stopwords_list = [
    'a', 'about', 'above', 'across', 'after', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also',
    'although', 'always', 'among', 'an', 'and', 'another', 'any', 'anybody', 'anyone', 'anything', 'anywhere', 'are',
    'area', 'areas', 'around', 'as', 'ask', 'asked', 'asking', 'asks', 'at', 'away', 'b', 'back', 'backed', 'backing',
    'backs', 'be', 'became', 'because', 'become', 'becomes', 'been', 'before', 'began', 'behind', 'being', 'beings',
    'best', 'better', 'between', 'big', 'both', 'but', 'by', 'c', 'came', 'can', 'cannot', 'case', 'cases', 'certain',
    'certainly', 'clear', 'clearly', 'come', 'could', 'd', 'did', 'differ', 'different', 'differently', 'do', 'does',
    'done', 'down', 'downed', 'downing', 'downs', 'during', 'e', 'each', 'early', 'either', 'end', 'ended', 'ending',
    'ends', 'enough', 'even', 'evenly', 'ever', 'every', 'everybody', 'everyone', 'everything', 'everywhere', 'f',
    'face', 'faces', 'fact', 'facts', 'far', 'felt', 'few', 'find', 'finds', 'first', 'for', 'four', 'from', 'full',
    'fully', 'further', 'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally', 'get', 'gets',
    'give', 'given', 'gives', 'go', 'going', 'good', 'goods', 'got', 'great', 'greater', 'greatest', 'group', 'grouped',
    'grouping', 'groups', 'h', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'herself', 'high', 'higher',
    'highest', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'important', 'in', 'interest', 'interested',
    'interesting', 'interests', 'into', 'is', 'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind', 'knew',
    'know', 'known', 'knows', 'l', 'large', 'largely', 'last', 'later', 'latest', 'least', 'less', 'let', 'lets', 'like',
    'likely', 'long', 'longer', 'longest', 'm', 'made', 'make', 'making', 'man', 'many', 'may', 'me', 'member', 'members',
    'men', 'might', 'more', 'most', 'mostly', 'mr', 'mrs', 'much', 'must', 'my', 'myself', 'n', 'necessary', 'need',
    'needed', 'needing', 'needs', 'never', 'new', 'newer', 'newest', 'next', 'no', 'nobody', 'non', 'noone', 'not',
    'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off', 'often', 'old', 'older', 'oldest', 'on', 'once',
    'one', 'only', 'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering', 'orders', 'other', 'others',
    'our', 'out', 'over', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps', 'place', 'places', 'point',
    'pointed', 'pointing', 'points', 'possible', 'present', 'presented', 'presenting', 'presents', 'problem', 'problems',
    'put', 'puts', 'q', 'quite', 'r', 'rather', 'really', 'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say',
    'says', 'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees', 'several', 'shall', 'she', 'should',
    'show', 'showed', 'showing', 'shows', 'side', 'sides', 'since', 'small', 'smaller', 'smallest', 'so', 'some',
    'somebody', 'someone', 'something', 'somewhere', 'state', 'states', 'still', 'such', 'sure', 't', 'take', 'taken',
    'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'these', 'they', 'thing', 'things', 'think',
    'thinks', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through', 'thus', 'to', 'today', 'together',
    'too', 'took', 'toward', 'turn', 'turned', 'turning', 'turns', 'two', 'u', 'under', 'until', 'up', 'upon', 'us',
    'use', 'used', 'uses', 'v', 'very', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way', 'ways', 'we', 'well',
    'wells', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'who', 'whole', 'whose', 'why', 'will',
    'with', 'within', 'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year', 'years', 'yet', 'you',
    'young', 'younger', 'youngest', 'your', 'yours', 'z'
]


        for row in reader:
             if row[3] in word_dictionary:
                new_string = row[2]
                for char in punctuation_chars:
                     new_string = new_string.replace(char, " ")
                lowercase_speech = new_string.lower()
                word_list = lowercase_speech.split()
                for word in word_list:
                     if word not in stopwords_list:
                          if word not in word_dictionary[row[3]]:
                            word_dictionary[row[3]][word] = 1
                          else:
                            word_dictionary[row[3]][word] += 1

        for pony in word_dictionary:
            word_dictionary[pony] = dict(filter(filter_function, word_dictionary[pony].items()))

        json.dump(word_dictionary, outfile)
        
if __name__ == "__main__":
    main()
                    

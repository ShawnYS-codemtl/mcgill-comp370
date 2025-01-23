import json 
import requests
import datetime

'''0401bcb262a248278ec5190c9535b805'''

NEWS_QUERY_STRING_TEMPLATE = "https://newsapi.org/v2/everything?q={}&from={}&apiKey={}"

def collect_news(api_key, news_keywords, lookback_days, output_path_json):
    data = fetch_latest_news(api_key, news_keywords, lookback_days)
    with open(output_path_json, 'w') as f:
        json.dump(data, f, indent = 4)


def calculate_lookback_date(lookback_days):
    lookback_date = datetime.datetime.now()
    return str(lookback_date.year) + "-" + str(lookback_date.month) + "-" + str(lookback_date.day - lookback_days)
 
'''
int -> str -> int -> list[dict]
'''
def fetch_latest_news(api_key, news_keywords, lookback_days=0):

    from_date = calculate_lookback_date(lookback_days)

    query_string = NEWS_QUERY_STRING_TEMPLATE.format(news_keywords,from_date,str(api_key))
    response = requests.get(query_string)

    if response.status_code != 200:
        raise Exception("unable to fetch latest news")
    
    if not news_keywords.replace("+", "X").isalpha():
        raise Exception("news_keywords can only have alphabetic characters")

    if response.json()['status'] == "error":
        raise Exception("request was unsuccessful") 
    
    return response.json()

if __name__ == "__main__":
    collect_news("0401bcb262a248278ec5190c9535b805","(The+AND+marvels+AND+Nia+AND+DaCosta+AND+review)",31, "marvels_review.json")
    
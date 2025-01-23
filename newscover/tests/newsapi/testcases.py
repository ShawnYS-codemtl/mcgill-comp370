import unittest
import sys
import datetime
sys.path.append('/Users/shawnyatsin/assignments/COMP370/hmk6/newscover')
from newsapi import fetch_latest_news



class FetchLatestNews(unittest.TestCase):

    def missing_news_keywords(self):
        self.assertRaises(Exception, fetch_latest_news("0401bcb262a248278ec5190c9535b805","", 10))

    def confirm_lookback_days(self):
        data = fetch_latest_news("0401bcb262a248278ec5190c9535b805","Trump+AND+trial", 10)
        from_date = datetime.datetime.now() - 10
        for article in data["articles"]:
            self.assertGreater(article['publishedAt'], from_date)
    
    def confirm_all_alphabetic(self):
        self.assertRaises(Exception, fetch_latest_news("0401bcb262a248278ec5190c9535b805","Trump+AND+tr1al", 10))





    


    

    

    
        

        

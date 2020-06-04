from twitterscraper import query_tweets
import datetime as dt 
import pandas as pd

begin_date = dt.date(2020, 1, 11)
end_date = dt.date(2020, 1, 30)

limit = 76000
lang = 'english'

tweets = query_tweets('Bitcoin AND BTC', begindate=begin_date, enddate=end_date, lang=lang, limit=limit)

df = pd.DataFrame(t.__dict__ for t in tweets)

file_name = 'data/range/BTC_tweets_' + str(begin_date) + '--' + str(end_date) + '.json'
df.to_json(file_name)
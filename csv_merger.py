import os
import glob
import pandas as pd

extension = 'csv'
all_filenames = [i for i in glob.glob('data/by_month/*.{}'.format(extension))]

print(all_filenames)

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv("data/combined_tweets.csv", index=False, encoding='utf-8')

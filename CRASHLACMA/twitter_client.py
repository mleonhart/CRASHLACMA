#!/usr/bin/python

import os
import shutil

from twitter_json_parser import TwitterJsonParser 

print("Running twitter client...")

for root, _, files in os.walk('../data_raw_tweets/'):
    for f in files:
        fullpath = os.path.join(root, f)
        print fullpath
        parser = TwitterJsonParser()
        print(parser.get_data_from_tweets(fullpath))
        shutil.move(fullpath, '../data_processed_tweets/')

		
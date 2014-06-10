#!/usr/bin/python

import os
import shutil

from twitter_json_parser import TwitterJsonParser 

read_dir = '../data_raw_tweets/'
write_dir = '../data_processed_tweets/'

print("Searching in %s for json tweet files") % read_dir

for root, _, files in os.walk(read_dir):
    for f in files:
        full_path = os.path.join(root, f)
        print '<3 ~ <3 ~ <3 ~ <3 ~ <3 ~ <3 ~ <3 ~ <3 ~ <3 ~ <3 ~ <3'
        print 'Parsing %s ' % full_path
        parser = TwitterJsonParser()
        print(parser.get_data_from_tweets(full_path))
        print 'Done parsing %s. Moving json file of tweets to %s' % (full_path, write_dir)
        shutil.move(full_path, write_dir)
        

		
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'YOUR CONSUMER KEY GOES HERE'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET GOES HERE'
ACCESS_KEY = 'YOUR ACCESS KEY GOES HERE'
ACCESS_SECRET = 'YOUR ACCESS SECRET GOES HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900) #Tweet every 15 min

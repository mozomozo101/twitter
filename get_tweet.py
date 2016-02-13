#!/usr/local/env python
# -*- coding: utf-8 -*-


from requests_oauthlib import OAuth1Session
from pprint import pprint
import json

CK='***'
CS='***'
AT='***'
AS='***'

# id指定でtweet取得
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'screen_name':'pet_bottle_bot'}


# 認証取る
twitter = OAuth1Session(CK, CS, AT, AS)

# getして来る
req = twitter.get(url, params = params)
#print(dir(req))
if req.status_code == 200:
	timeline = json.loads(req.text)
	for tweet in timeline:
		print(tweet["text"])

else:
	print ("Error: %d" % req.status_code)

#!/usr/bin/env python3

import tweepy
import auth
import random

API_KEY = auth.get_api_key()
SECRET = auth.get_secret()
BEARER = auth.get_bearer_token()
ACCESS = auth.get_access_token()
ACCESS_SECRET = auth.get_access_token_secret()

oauth = tweepy.OAuthHandler(API_KEY, SECRET)
oauth.set_access_token(ACCESS, ACCESS_SECRET)

api = tweepy.API(oauth)

stamp = random.random() * 10

if stamp < 5:
    api.update_status(status="@yesitsjaden_ who asked?\n" + str(stamp))
else:
    api.update_status(status="@yesitsjaden_ did i ask?\n" + str(stamp))

print("done :)")

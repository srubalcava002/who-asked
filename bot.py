#!/usr/bin/env python3

import tweepy
import auth

API_KEY = auth.get_api_key()
SECRET = auth.get_secret()
BEARER = auth.get_bearer_token()
ACCESS = auth.get_access_token()
ACCESS_SECRET = auth.get_access_token_secret()

print("[DEBUG]\tUSING:")
print("API KEY: " + API_KEY)
print("SECRET KEY: " + SECRET)
print("ACCESS TOKEN: " + ACCESS)
print("ACCESS SECRET: " + ACCESS_SECRET)

oauth = tweepy.OAuthHandler(API_KEY, SECRET)
oauth.set_access_token(ACCESS, ACCESS_SECRET)

api = tweepy.API(oauth)

api.update_status(status="@yesitsjaden_ who asked?")
print("done :)")

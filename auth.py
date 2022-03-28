import os
import sys
import auth
AUTH_FILE = os.getcwd() + "/creds"
BOT_CREDS = os.getcwd()  + "/bot_creds"

def get_secret():
    with open(AUTH_FILE, "r") as file:
       secret = file.readline()
       return file.readline()[:-1]

def get_api_key():
    with open(AUTH_FILE, "r") as file:
        return file.readline()[:-1]

def get_bearer_token():
    with open(AUTH_FILE, "r") as file:
        bear = file.readline()
        bear = file.readline()
        return file.readline()[:-1]

def get_access_token():
    with open(BOT_CREDS, "r") as file:
        return file.readline()[:-1]

def get_access_token_secret():
    with open(BOT_CREDS, "r") as file:
        secret = file.readline()
        return file.readline()[:-1]

if __name__ == "__main__":
    print("secret key: " + get_secret())
    print("api key: " + get_api_key())
    print("bearer token: " + get_bearer_token())

    print("bot access: " + get_access_token())
    print("bot secret: " + get_access_token_secret())

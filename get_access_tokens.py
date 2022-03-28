# A TOOL TO GET USER ACCESS TOKENS
import tweepy
import auth as authorization

oauth1_user_handler = tweepy.OAuth1UserHandler(
    authorization.get_api_key(), authorization.get_secret(),
    callback="https://172.0.0.1"
)

print(oauth1_user_handler.get_authorization_url())
oauth_verifier = input("verifier: ")

access_token, access_token_secret = oauth1_user_handler.get_access_token(oauth_verifier)

print("access token: " + access_token)
print("access token secret: " + access_token_secret)


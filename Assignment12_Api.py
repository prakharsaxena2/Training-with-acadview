'''Q1'''
'''The Access Token is a credential that can be used by an application to access an API.
    It can be any type of token (such as an opaque string or a JWT) and is meant for an API. Its purpose is to inform the
 API that the bearer of this token has been authorized to access the API and perform specific actions (as specified by the
 scope that has been granted).
    The Access Token should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API.
    Access token from my Twitter API - 924160409728200704-W3y0l4s9bgp8mnExmNvIs90LK4gw4u2
'''


'''Q2'''
'''
    Google -> 172.217.31.14
    Facebook -> 157.240.13.35
'''

'''Q3'''
import tweepy
'''Impotring tweepy module'''

consumer_key = "************"
consumer_secret = "**************************"
'''Giving Consumer key and consummer Secret'''

access_token = "*****************************"
access_token_secret = "**********************************************************88"
'''Giving Access Token and Access tokwn secret'''

'''Authorization to consumer key and consumer secret'''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

'''Access to user's access key and access secret'''
auth.set_access_token(access_token, access_token_secret)

'''Calling api'''
api = tweepy.API(auth)

'''Searching for tweets  with keyword'''
public_tweets = api.search("Modi")

'''Printing tweets'''
for tweets in public_tweets:
    print(tweets.text)


'''Q4'''
'''A library is a collection of functions / objects that serves one particular purpose.You could use a
    library in a variety of projects.
    whereas
   An API is an interface for other programs to interact with your program or library  without having
    direct access. '''




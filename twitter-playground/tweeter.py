import twitter
from credentials import API_KEY, API_SECRET, ACCESS_KEY, ACCESS_SECRET

api = twitter.Api(
    consumer_key = API_KEY, 
    consumer_secret = API_SECRET,
    access_token_key = ACCESS_KEY,
    access_token_secret = ACCESS_SECRET)

def send_tweet(tweet):
    '''
    Production Function, use to submit to Twitter Endpoint
    '''
    status = api.PostUpdate(tweet)

def send_mock_tweet(tweet):
    '''
    Use for testing, does not send to Twitter Endpoint
    Only sends to console as a print
    '''
    print(status)

def get_mentions_tweet():
    mention = api.GetMentions(count=1)
    return mention
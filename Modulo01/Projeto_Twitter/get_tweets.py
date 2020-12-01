import config
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

consumer_key = config.twitter_api_key
consumer_secret = config.twitter_api_secret_key

access_token = config.twitter_access_token
access_token_secret = config.twitter_access_token_secret

# Arquivo de saída com os Tweets
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets{data_hoje}.txt", "w")


# Conexão com Tweets
class MyListener(StreamListener):

    def on_data(self, data):
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["Trump"])

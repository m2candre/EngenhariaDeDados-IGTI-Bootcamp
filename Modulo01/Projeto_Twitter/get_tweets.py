import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

consumer_key = "Lk7l1MmTSwJv03s8Mv5CkRNml"
consumer_secret = "sLnhiWcxlj5gRApaUSe9wWKRfzN4tbnEsGAGlvu7xmnp57Msr0"

access_token = "1331006111349141508-LdrrMlEpEhUs2Ul9PanVMSPXNfitl8"
access_token_secret = "MPvwLKlV4Z5MoanxivPpZvpSHPpRbN6hkdKBygp3APxeh"

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

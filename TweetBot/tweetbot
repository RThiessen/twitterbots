import csv
import datetime
import time
import twitter

ACCESS_TOKEN = ""
ACCESS_TOKEN_SEC = ""
CON_KEY = ""
CON_SEC = ""
 
my_auth = twitter.OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SEC,CON_KEY,CON_SEC)
twit = twitter.Twitter(auth=my_auth)
tweet ="testing"
twit.statuses.update(status=tweet)
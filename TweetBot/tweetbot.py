import csv
import datetime
import time
import twitter

TOKEN = ""
TOKEN_KEY = ""
CON_SEC = ""
CON_SEC_KEY = ""
 
my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
twit = twitter.Twitter(auth=my_auth)
tweet ="testing"
twit.statuses.update(status=tweet)
# Chapter 03: Diving Deep into Twitter API

## API Authentication
The package tweepy is great at handling all the Twitter API OAuth Authentication details for you. All you need to do is pass it your authentication credentials. In this interactive exercise, we have created some mock authentication credentials (if you wanted to replicate this at home, you would need to create a <a href="https://apps.twitter.com/"> Twitter App </a> as Hugo detailed in the video). Your task is to pass these credentials to tweepy's OAuth handler.

### Instruction:
* Import the package tweepy.
* Pass the parameters consumer_key and consumer_secret to the function tweepy.OAuthHandler().
* Complete the passing of OAuth credentials to the OAuth handler auth by applying to it the method set_access_token(), along with arguments access_token and access_token_secret.

#### Script
```
# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

```
##### Comment:
Awesome!

## Streaming tweets
Now that you have set up your authentication credentials, it is time to stream some tweets! We have already defined the tweet stream listener class, MyStreamListener, just as Hugo did in the introductory video. You can find the code for the tweet stream listener class here.

Your task is to create the Streamobject and to filter tweets according to particular keywords.

### Instructions:
* Create your Stream object with authentication by passing tweepy.Stream() the authentication handler auth and the Stream listener l;
* To filter Twitter streams, pass to the track argument in stream.filter() a list containing the desired keywords 'clinton', 'trump', 'sanders', and 'cruz'.

#### Script:
```
# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])
```
##### Comment:
Awesome!

## Load and explore your Twitter data
Now that you've got your Twitter data sitting locally in a text file, it's time to explore it! This is what you'll do in the next few interactive exercises. In this exercise, you'll read the Twitter data into a list: tweets_data.

### Instructions:
* Assign the filename 'tweets.txt' to the variable tweets_data_path.
* Initialize tweets_data as an empty list to store the tweets in.
* Within the for loop initiated by for line in tweets_file:, load each tweet into a variable, tweet, using json.loads(), then append tweet to tweets_data using the append() method.
* Hit submit and check out the keys of the first tweet dictionary printed to the shell.

#### Script
```
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())
```

#### Output:
```
<script.py> output:
    dict_keys(['retweet_count', 'user', 'place', 'favorited', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'geo', 'in_reply_to_status_id', 'created_at', 'coordinates', 'source', 'text', 'entities', 'in_reply_to_status_id_str', 'contributors', 'retweeted_status', 'id_str', 'lang', 'id', 'timestamp_ms', 'favorite_count', 'is_quote_status', 'truncated', 'retweeted', 'possibly_sensitive', 'extended_entities', 'filter_level'])
```
##### Comment:
Awesome!

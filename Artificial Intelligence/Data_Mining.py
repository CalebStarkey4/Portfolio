from itertools import count
import tweepy
import keys
import sys
from textblob import TextBlob
from OpenMapQuest import get_geocodes
import preprocessor as p
import numpy as np
import pandas as pd
import folium

client = tweepy.Client(bearer_token = keys.bearer_token)

# Check if there are command line arguments and set my_query accordingly
my_query = f"{sys.argv[1]} -is:retweet" if len(sys.argv) > 1 else "covid -is:retweet"

# Retrieve 100 recent tweets - be sure to include location and language information.
response = client.search_recent_tweets(query = my_query, max_results = 100, user_fields = ["location"], tweet_fields = ["lang"], expansions = ["author_id"])

# Set preprocessor options
p.set_options(p.OPT.MENTION, p.OPT.EMOJI, p.OPT.HASHTAG, p.OPT.NUMBER, p.OPT.RESERVED, p.OPT.SMILEY, p.OPT.URL)

# Create a 2D list to hold the cleaned tweets and a counter to facilitate adding lists to it
data = []

# Create a set of all the locations to minimize use of OpenMapQuest
users = {u["id"]:u for u in response.includes["users"]}
locations = {np.nan:{"latitude":np.nan, "longitude":np.nan}}
places = set()
for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        if user.location and not user.location in locations:
            places.add(user.location)
            locations[user.location] = {"latitude":np.nan, "longitude":np.nan}

# Loop through the locations and convert them to latitude and longitude if possible
bad_locations = get_geocodes(places, locations)

# Loop through the tweets
for tweet in response.data:
    cleaned_text = p.clean(tweet.text) # Use the preprocessor to "clean" each tweet. Use ALL the fields shown on p542
    # If the language field of the tweet is not English, use a TextBlob to translate.
    if tweet.lang != "en":
        try:
            cleaned_text = str(TextBlob(cleaned_text).translate(to = "en"))
        except:
            pass # If translation fails, leave it in the foreign language
    # Add to 2D list
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        if user.location != None: # If a location was provided
            loc = [user.location, locations[user.location]["latitude"], locations[user.location]["longitude"]] # Find its latitude and longitude in locations
        else: # Else, set the location, latitude, and longitude to np.nan
            loc = [np.nan] * 3
    info = [user.username, cleaned_text, tweet.lang]
    data.append(info + loc)

# Convert to a DataFrame
tweets = pd.DataFrame(data, columns = ["username", "tweet", "lang", "location", "latitude", "longitude"])

# Report statistics on how many tweets had convertible location data, and how many were in a foreign language.
loc_bools = tweets.apply(lambda x : True if np.isnan(x['latitude']) else False, axis = 1)
has_location_data = len(tweets) - len(loc_bools[loc_bools == True].index)
en_bools = tweets.apply(lambda x : True if x['lang'] != 'en' else False, axis = 1)
english_tweets = len(en_bools[en_bools == True].index)
print(f"{(has_location_data / len(tweets)) * 100}% of tweets contain location data ({has_location_data} / {len(tweets)})")                             
print(f"{(english_tweets / len(tweets)) * 100}% of tweets are non-English ({english_tweets} / {len(tweets)})")

# Remove all the rows with NaN
tweets.dropna(inplace = True)

# Create the map (html) file using the folium library.
map = folium.Map(location = [39.8283, -98.5795],
                 tiles = "Stamen Terrain",
                 zoom_start = 5, detect_retina = True)
for t in tweets.itertuples():
    text = ": ".join([t.username, t.tweet])
    popup = folium.Popup(text, parse_html = True)
    marker = folium.Marker((t.latitude, t.longitude), popup = popup)
    marker.add_to(map)
map.save("tweet_map.html")
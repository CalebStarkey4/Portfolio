from geopy import OpenMapQuest
import time
import keys

def get_geocodes(places, locations):
    """Get the latitude and longitude for each tweet's location.
    Returns the number of tweets with invalid location data."""
    print('Getting coordinates for tweet locations...')
    geo = OpenMapQuest(api_key=keys.mapquest_key)  # geocoder
    bad_locations = 0  

    for place in places:
        processed = False
        delay = .1  # used if OpenMapQuest times out to delay next call
        while not processed:
            try:  # get coordinates for tweet['location']
                geo_location = geo.geocode(place)
                processed = True
            except:  # timed out, so wait before trying again
                print('OpenMapQuest service timed out. Waiting.')
                time.sleep(delay)
                delay += .1

        if geo_location:  
            locations[place]['latitude'] = geo_location.latitude
            locations[place]['longitude'] = geo_location.longitude
        else:  
            bad_locations += 1  # tweet['location'] was invalid
    
    print('Done geocoding')
    return bad_locations

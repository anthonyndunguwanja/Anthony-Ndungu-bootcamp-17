import json
import urllib2

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
def get_data():
    url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
    data = json.load(urllib2.urlopen(url))

# print the result
    print data
get_data()


#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI


#Author: T Shrinivasan <tshrinivasan@gmail.com>


# get api from here  https://developers.facebook.com/tools/explorer


api = "EAACEdEose0cBAI4mvm8ZCpa2Ahid1tg0OqjJFSu1AlLfb0ZCDJvkFwQZCgo1YNyXR9N3bmUDLFMC5gZBZChYKKsTttVQ3QiVBTTyOP1XDAnRW5YsYCMKmysNUVrjwNB30l2lGdOKOxCrolY8VpHZA1mTxjOdKR4ze22ro4vUWfOQZDZD"







graph = GraphAPI(api)

message = '''Thanks for joining







'''


# Find the ids of your desired groups from http://lookup-id.com/  
# and add this in this array groups

groups = [ '543897769110125', 'groupid2', 'groupid3']



for group_id in groups:
	print "Posting to " + 'http://www.facebook.com/groups/' + str(group_id)
	graph.post(path =str(group_id) + '/feed', message=message)
	time.sleep(10)
print "Done"

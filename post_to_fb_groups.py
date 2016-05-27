#-*- coding: utf-8 -*-
import time
from facepy import GraphAPI


#Author: T Shrinivasan <tshrinivasan@gmail.com>


# get api from here  https://developers.facebook.com/tools/explorer


api = "EAACEdEose0cBAOKn6UfcG1LvT99iZCnHWUlP5KZCyEb1N8UwVbrTOebM6UeLbwUZATgDED2PZCyB5tuF2BKyCgMILrx98Hym1gXUdgRIfscloqwSTdTUeaZAv1p45G0JaWCxlYahRIsll2FbjST1orPA5PHnpKJ4hypJW4toZAaQZDZD"







graph = GraphAPI(api)

message = 'Thanks for joining'


Add all your contents to be posted to facebook groups here




'''


# Find the ids of your desired groups from http://lookup-id.com/  
# and add this in this array groups

groups = [ '543897769110125', 'groupid2', 'groupid3']



for group_id in groups:
	print "Posting to " + 'http://www.facebook.com/groups/' + str(group_id)
	graph.post(path =str(group_id) + '/feed', message=message)
	time.sleep(10)
print "Done"

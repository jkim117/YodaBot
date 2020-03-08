#!/usr/bin/env/python

#-----------------------------------------------------
# yoda.py
# Author: Jason Kim
#-----------------------------------------------------
import requests
import random

def main():
	url = 'https://api.groupme.com/v3/bots/post'

	images = ['https://media1.tenor.com/images/ad939c1055c9679e084248bc05fd7dc8/tenor.gif?itemid=15592289', 'https://media1.tenor.com/images/a32146f4fd280db7636a601eec18bdbc/tenor.gif?itemid=15699485', 'https://media1.tenor.com/images/34518d08bf593b3848e72e4b8ce57c67/tenor.gif?itemid=15610894', 'https://media1.tenor.com/images/fbd76ba048706eeaa0d39ba36fe8b100/tenor.gif?itemid=15688894', 'https://data.whicdn.com/images/338155991/original.gif', 'https://i.imgur.com/qsjx2bQ.gif', 'https://i.pinimg.com/originals/40/b9/04/40b90467b637148ce471a5d4bc454151.gif', 'https://i.pinimg.com/originals/3a/13/01/3a1301b68d7c39802ee3a20c81a1566a.gif', 'https://media1.tenor.com/images/771e7d17fb971feb779646bb11280d3f/tenor.gif?itemid=5463195']
	randImg = random.randint(0, len(images) - 1)

	messages = ['Eat I must.', 'Eat or eat. There is no starve.', 'Hunger is the path to the dark side.', 'Hunger leads to anger, anger leads to hate, hate leads to suffering.', 'Adventure, excitement. A jedi craves not these things. Donuts, a jedi should crave.', 'A jedi uses the force for eating and satisfaction, never for attack.', 'Soon I will eat.', 'For my ally is food and a powerful ally it is.', 'Once you start down the path of hunger, forever will it dominate your destiny.', 'Eat, good food, I must. Yessss.']
	randMesage = random.randint(0, len(messages) - 1)

	time = random.randint(45, 60)
	finalTime = '5:'+str(time)
	if (time == 60):
		finalTime = '6:00'

	finalMessage = finalTime + '. ' + messages[randMesage]
	
	myMessage = {
		"bot_id"  : "8600598b4736f9748065663205",
		"text"    : finalMessage,
		"picture_url" : images[randImg]
	}
	x = requests.post(url, data = myMessage)

if __name__ == '__main__':
	main()
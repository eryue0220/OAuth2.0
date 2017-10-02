#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import httplib2
import json
from gecode import get_geo_code_location
import os
import sys
import codecs
from datetime import date

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)
secret_keys = json.loads(open('secrets.json', 'r').read())
google_secret_key = secret_keys['google_secret_key']
client_id = secret_keys['foursquare_secret_key']['client_id']
client_key = secret_keys['foursquare_secret_key']['client_key']
today = date.today()

if today.day > 10:
    day = today.day
else:
    day = '0' + str(today.day)

current = '%s%s%s' % (today.year, today.month, day)


def findARestaurant(mealType, location):
    latitude, longitude = get_geo_code_location(google_secret_key, location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&query=%s&v=%s' %
		(client_id, client_key, latitude, longitude, mealType, current))
    h = httplib2.Http()
    data = json.loads(h.request(url, 'GET')[1])

    if data['response']['venues']:
        result = data['response']['venues'][0]
        restaurant_id = result['id']
        img_url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((restaurant_id,client_id,client_key)))
        img = json.loads(h.request(img_url, 'GET')[1])
        address = ''

        for i in result['location']['formattedAddress']:
            address += i + " "
        restaurant_address = address

        if img['response']['photos']['items']:
            firstpic = img['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            imageURL = prefix + "300x300" + suffix
        else:
            imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"

        print "Restaurant Name: %s" % result['name']
        print "Restaurant Address: %s" % restaurant_address
        print "Image: %s \n" % imageURL
        return {
            'name': result['name'],
            'address': result['location']['formattedAddress'],
            'img_url': imageURL
        }
    else:
        print('No Result Match')
        return None


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney Australia")

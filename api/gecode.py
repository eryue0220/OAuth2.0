#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import httplib2
import json

def get_geo_code_location(google_api_key, input):
    location_string = input.replace(' ', '+')
    url = ('https://maps.googleapis.com/maps/api/geocode/json?' +
        'address=%s&key=%s' % (location_string, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    location = result['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
    return (latitude, longitude)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py

from newsapi import NewsApiClient
import serial
import time
from datetime import datetime
#from subprocess import call


s = datetime.now().strftime('%Y')[2:] + '0' + datetime.now().strftime('%w%m%d%H%M%S')
print(s)

#serial = serial.Serial(port = '/dev/rfcomm0', 
						#baudrate=38400, 
						#parity=serial.PARITY_NONE,
						#stopbits=serial.STOPBITS_ONE,
						#bytesize=serial.EIGHTBITS,
						#timeout=1)

#serial.write('Connected\n')

newsapi = NewsApiClient(api_key='b5a3ea3530de476cb0a17415ff59cd16')

while True:
    s = str(newsapi.get_top_headlines(language='en', q = 'tech'))

    while (s.find('title') > 0):
        print(s[s.find('title') + 10 : s.find('url') - 5])
        #serial.write(s[s.find('title') + 10 : s.find('url') - 5].encode('ascii')+'\n')
        time.sleep(5)
        s = s[s.find('url') + 2:]




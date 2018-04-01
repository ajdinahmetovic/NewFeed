from newsapi import NewsApiClient
import serial
import time


#serial = serial.Serial(port = '/dev/rfcomm0', baudrate=38400)
newsapi = NewsApiClient(api_key='b5a3ea3530de476cb0a17415ff59cd16')

while True:
    s = str(newsapi.get_top_headlines(language='en', q = 'tech'))

    while (s.find('title') > 0):
        print(s[s.find('title') + 9 : s.find('description') - 4])
        #serial.write(s[s.find('title') + 9 : s.find('description') - 4])
        s = s[s.find('description') + 2:]
        time.sleep(20)

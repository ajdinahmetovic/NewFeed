from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b5a3ea3530de476cb0a17415ff59cd16')

s = str(newsapi.get_top_headlines(q='tech'))

while (s.find('title') > 0):
    print(s[s.find('title') + 9 : s.find('description') - 4])
    s = s[s.find('description') + 2:]
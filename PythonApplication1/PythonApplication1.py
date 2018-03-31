
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b5a3ea3530de476cb0a17415ff59cd16')

print(newsapi.get_top_headlines(q='tech'))


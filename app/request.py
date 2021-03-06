from concurrent.futures import process
from app import app
import urllib.request, json
from .models import news 


News = news.News

#getting api key
api_key = app.config['MOVIE_API_KEY']

# getting the news base url
base_url = app.config['MOVIE_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json repsonse to our url request
    '''
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

        return news_results

    
def process_results (news_list):
    '''
    Function that processes the news reults and transforms them to a list of objects

    Args: 
        news_list:  a list of dictionaries that contain news details 

    Returns:
        news_results: A list of news objects 
    '''

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')
        time = news_item.get('time')

        if poster: 
            news_object = News(id, title, overview, poster, vote_average, vote_count, time)
            news_results.append(news_object)

    return news_results
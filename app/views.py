from flask import render_template
from app import app
from .request import get_news

#views 
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

       #Getting popular news 
    popular_news = get_news('popular')
    print(popular_news)


    title = 'Home - Catch up with what is around you anywhere'
 

    return render_template('index.html', title = title, popular = popular_news)
@app.route('/newstoday/<news_id>')
def news(news_id):
    '''
    View the news page function that returns the news details page and its data
    '''
    return render_template('index.html', id = news_id)
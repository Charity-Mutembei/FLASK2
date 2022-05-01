import unittest
from models import news
News = news.News 

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behavior of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News(1234, 'Python Must be Crazy', 'A thrilling new python series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self): 
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()

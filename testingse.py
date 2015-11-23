"Testing of search engine"
import application
import unittest

class TestSearchEngine(unittest.TestCase):

    def test_(self):
        self.assertEqual(application.page_name( 'www.wikipedia.com'),True)

if __name__ == '__main__':
    unittest.main()

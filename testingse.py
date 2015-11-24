"Testing of search engine"
import application
import unittest

class TestSearchEngine(unittest.TestCase):

    def test_length(self):
        self.assertGreater (4, 1)


if __name__ == '__main__':
    unittest.main()

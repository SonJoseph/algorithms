import unittest
from cache import getEvicted

class TestCache(unittest.TestCase):

    def test_getEvicted(self):
        requests = ['a', 'a', 'b', 'c', 'a', 'c', 'b', 'a']
        cache_size = 2
        evicted = getEvicted(requests, cache_size)

        self.assertEqual(evicted, ['b', 'c'])

if __name__ == '__main__':
    unittest.main()
#!/usr/bin/python3
"""lifo cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """BaseCaching"""
    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ Add an item"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ Get an item"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            val = self.cache_data[key]
            return val

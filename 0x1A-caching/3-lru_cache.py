#!/usr/bin/python3
"""lru cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """BaseCaching"""
    def __init__(self):
        super().__init__()
        self.head, self.tail = '-', '='
        self.next, self.prev = {}, {}
        self.connect(self.head, self.tail)

    def put(self, key, item):
        """Add an item"""
        if key and item:
            if key in self.cache_data:
                self._remove(key)
            self._add(key, item)

    def _remove(self, key):
        """Remove an item"""
        self.connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache_data[key]

    def connect(self, x, y):
        """connect items"""
        self.next[x], self.prev[y] = y, x

    def _add(self, key, item):
        """ Add an item"""
        self.cache_data[key] = item
        self.connect(self.prev[self.tail], key)
        self.connect(key, self.tail)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.next[self.head]))
            self._remove(self.next[self.head])

    def get(self, key):
        """Get an item"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            val = self.cache_data[key]
            self._remove(key)
            self._add(key, val)
            return val

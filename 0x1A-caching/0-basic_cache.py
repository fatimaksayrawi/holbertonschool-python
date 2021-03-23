#!/usr/bin/python3
"""basic cache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BaseCaching"""
    def put(self, key, item):
        """Add an item"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)

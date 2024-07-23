#!/usr/bin/env python3
"""Basic caching module."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class that supports storing and retrieving items."""

    def put(self, key, value):
        """Add an item to the cache.
        
        Args:
            key: The key under which the item is stored.
            value: The item to store in the cache.
        """
        if key is None or value is None:
            return
        self.cache_data[key] = value

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)

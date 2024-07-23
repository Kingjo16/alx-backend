#!/usr/bin/env python3
"""Last-In First-Out caching module."""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents a LIFO caching system."""
    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, value):
        """Add an item to the cache.

        Args:
            key: The key under which the item is stored.
            value: The item to store in the cache.
        """
        if key is None or value is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", last_key)
        self.cache_data[key] = value
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key, None)

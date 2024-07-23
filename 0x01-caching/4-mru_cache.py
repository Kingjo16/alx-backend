#!/usr/bin/env python3
"""Most Recently Used caching module."""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents a MRU caching system."""

    def __init__(self):
        """Initialize the MRU cache."""
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
                mru_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", mru_key)
        self.cache_data[key] = value
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None

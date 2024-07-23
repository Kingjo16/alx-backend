#!/usr/bin/env python3
"""Least Recently Used caching module."""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represents a LRU caching system."""

    def __init__(self):
        """Initialize the LRU cache."""
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
                lru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", lru_key)
        else:
            self.cache_data.move_to_end(key, last=False)
        self.cache_data[key] = value

    def get(self, key):
        """Retrieve an item from the cach."""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None

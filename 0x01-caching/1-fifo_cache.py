#!/usr/bin/env python3
"""First-In First-Out caching module."""

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represents a FIFO caching system.

    This class provides methods to store and retrieve items
    using a FIFO removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initialize the FIFO cache."""
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
        self.cache_data[key] = value
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieve an item from the catch."""
        return self.cache_data.get(key, None)

#!/usr/bin/env python3
"""Least Frequently Used caching module."""

from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents a LFU caching system.

    This class provides methods to store and retrieve items
    using a LFU removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_frequency = []

    def __reorder_items(self, key):
        """Reorder the items in the cache based on usage frequency.

        Args:
            key: The key of the item that was most recently used.
        """
        max_positions = []
        key_frequency = 0
        key_position = 0
        insert_position = 0

        for i, (cached_key, frequency) in enumerate(self.key_frequency):
            if cached_key == key:
                key_frequency = frequency + 1
                key_position = i
                break
            elif not max_positions or frequency < self.key_frequency[max_positions[-1]][1]:
                max_positions.append(i)

        max_positions.reverse()
        for pos in max_positions:
            if self.key_frequency[pos][1] > key_frequency:
                break
            insert_position = pos

        self.key_frequency.pop(key_position)
        self.key_frequency.insert(insert_position, [key, key_frequency])

    def put(self, key, value):
        """Add an item to the cache.

        Args:
            key: The key under which the item is stored.
            value: The item to store in the cache.
        """
        if key is None or value is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.key_frequency.pop()
                self.cache_data.pop(lfu_key)
                print("DISCARD:", lfu_key)

            self.cache_data[key] = value
            insert_index = len(self.key_frequency)
            for i, (cached_key, frequency) in enumerate(self.key_frequency):
                if frequency == 0:
                    insert_index = i
                    break
            self.key_frequency.insert(insert_index, [key, 0])
        else:
            self.cache_data[key] = value
            self.__reorder_items(key)

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item stored under the provided key, or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
            return self.cache_data[key]
        return None

#!/usr/bin/env python3
"""A script that helps with pagination."""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the std the end index (exclusive)."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Class server for pagination."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page from the dataset."""
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

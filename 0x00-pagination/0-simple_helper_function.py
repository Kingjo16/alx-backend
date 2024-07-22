#!/usr/bin/env python3
"""Function That will help the Pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Index Reciver for range from a given page and page size."""
    enter = (page - 1) * page_size
    finsh = enter + page_size
    return (enter, finsh)

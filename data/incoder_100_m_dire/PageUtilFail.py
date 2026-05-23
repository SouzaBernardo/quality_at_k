class PageUtil: 
    def __init__(self, data, page_size):
        """
        Initialize the PageUtil object with the given data and page size.
        :param data: list, the data to be paginated
        :param page_size: int, the number of items per page
        """
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size



    def get_page(self, page_number):
        """
        Retrieve a specific page of data.
        :param page_number: int, the page number to fetch
        :return: list, the data on the specified page
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page(1)
        [1]

        """
        start = page_number * self.page_size
        end = start + self.page_size
        if end > self.total_items:
            end = self.total_items
        return self.data[start:end]


    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page_info(1)
        >>> {
        >>>     "current_page": 1,
        >>>     "per_page": 1,
        >>>     "total_pages": 4,
        >>>     "total_items": 4,
        >>>     "has_previous": False,
        >>>     "has_next": True,
        >>>     "data": [1]
        >>> }

        """
        page_number = int(page_number)
        per_page = self.page_size
        current_page = page_number - 1
        if current_page < 0:
            current_page = 0
        has_next = (current_page + per_page) < self.total_pages
        has_previous = current_page > 0
        return {
            "current_page": current_page,
            "per_page": per_page,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": self.data[current_page * per_page: (current_page + 1) * per_page]
        }


    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.search("1")
        >>> search_info = {
        >>>     "keyword": "1",
        >>>     "total_results": 1,
        >>>     "total_pages": 1,
        >>>     "results": [1]
        >>> }
        """
        matching_items = []
        matching_count = 0
        for item in self.data:
            if keyword in str(item):
                matching_count += 1
                matching_items.append(item)
        return {
            "keyword": keyword,
            "total_results": matching_count,
            "total_pages": self.total_pages,
            "results": matching_items
        }
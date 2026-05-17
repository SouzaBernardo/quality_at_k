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
        page_info = self.get_page_info(page_number)
        return page_info[0]


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
        page_info = {}
        if page_number > self.total_pages:
            raise PageNumberOutOfRangeError("Page number is out of range.")
        if page_number < 1:
            raise PageNumberOutOfRangeError("Page number is out of range.")
        page_info["current_page"] = page_number
        page_info["per_page"] = self.page_size
        page_info["total_pages"] = self.total_pages
        page_info["total_items"] = self.total_items
        page_info["has_previous"] = self.data[page_number - 1]
        page_info["has_next"] = self.data[page_number]
        page_info["data"] = self.data[page_number - 1:page_number]
        return page_info


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
        page_info = self.get_page_info(page_number)
        search_info = self.get_page_info(page_number)
        search_info["keyword"] = keyword
        search_info["total_pages"] = self.total_pages
        search_info["total_results"] = self.total_items
        search_info["results"] = self.data[page_number-1:page_number]
        return search_info
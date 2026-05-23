class PageUtil:  
    """
    PageUtil class is a versatile utility for handling pagination and search functionalities in an efficient and convenient manner.
    """

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
        """
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError("Invalid page number")
        
        if page_number == 1:
            self.data = [self.data[i] for i in range(self.total_items)]
        else:
            self.data = [self.data[i] for i in range(page_number * self.page_size, self.total_items, self.page_size)]
        
        return self.data

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
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError("Invalid page number")
        
        if page_number == 1:
            self.data = [self.data[i] for i in range(self.total_items)]
        else:
            self.data = [self.data[i] for i in range(page_number * self.page_size, self.total_items, self.page_size)]
        
        return {
            "current_page": page_number,
            "per_page": self.page_size,
            "total_pages": self.total_pages,
            "total_items": self.total_items,
            "has_previous": self.page_size > 1,
            "has_next": self.page_size > 1,
            "data": self.data
        }

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        """
        total_results = 0
        total_pages = 0
        for item in self.data:
            if keyword in item:
                total_results += 1
                total_pages += 1
        
        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": self.data[total_pages:total_pages + self.page_size]
        }
        return search_info
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
        >>> page_util = PageUtil([1, 2, 3, 4], 1)
        >>> page_util.get_page(1)
        [1]

        """
        page_index = page_number - 1
        if page_index < 0:
            page_index = 0
        page_size = min(self.page_size, self.total_items - page_index - 1)
        if page_size < 1:
            page_size = 1
        page_start = page_index * page_size
        page_end = page_start + page_size
        if page_end > self.total_items:
            page_end = self.total_items
        return [self.data[page_start:page_end]]
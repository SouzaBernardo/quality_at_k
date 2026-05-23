
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
        total_items, total_pages, page_number, page_size = self.get_page_info(page_number)
        if page_number < 0 or page_number >= total_pages:
            raise ValueError("Page number is out of range.")
        if page_number % page_size != 0:
            raise ValueError("Page size must be a multiple of the page number.")
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        return self.data[start_index:end_index]



    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        """
        matching_items = []
        total_results = 0
        for item in self.data:
            if keyword in item:
                total_results += 1
                matching_items.append(item)
        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_results // self.page_size + 1,
            "results": matching_items
        }
        return search_info
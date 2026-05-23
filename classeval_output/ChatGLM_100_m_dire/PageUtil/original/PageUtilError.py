
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
        """
        if page_number < 1 or page_number > self.total_pages:
            raise ValueError("Invalid page number")

        if page_number == 1:
            self.data[page_number - 1] = self.get_page_info(page_number - 1)
        else:
            self.data[page_number - 1] = []

        return self.get_page_info(page_number - 1)

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        """
        current_page = self.total_pages // self.page_size
        total_pages = self.total_pages % self.page_size
        total_items = self.data.count(page_number)
        has_previous = self.page_size - (page_number - current_page) > 0
        has_next = self.page_size - (page_number + 1) > 0
        return {
            "current_page": current_page,
            "per_page": total_pages // self.page_size,
            "total_pages": total_pages,
            "total_items": total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": self.data[page_number:current_page]
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
            "results": [self.get_page(page_number) for page_number in range(self.total_pages)]
        }
        return search_info
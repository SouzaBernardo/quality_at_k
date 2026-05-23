
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
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]
    

    def get_page_info(self, page_number):
        """
        Retrieve information about a specific page.
        :param page_number: int, the page number to fetch information about
        :return: dict, containing page information such as current page number, total pages, etc.
        """
        current_page = page_number
        per_page = self.page_size
        total_pages = self.total_pages
        total_items = self.total_items
        has_previous = page_number > 1
        has_next = page_number < total_pages
    
        start_index = (page_number - 1) * per_page
        end_index = start_index + per_page
        data = self.data[start_index:end_index]
    
        page_info = {
            "current_page": current_page,
            "per_page": per_page,
            "total_pages": total_pages,
            "total_items": total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": data
        }
    
        return page_info
    

    def search(self, keyword):
        """
        Search for items in the data that contain the given keyword.
        :param keyword: str, the keyword to search for
        :return: dict, containing search information such as total results and matching items
        """
        matching_items = [item for item in self.data if keyword in str(item)]
        total_results = len(matching_items)
        total_pages = (total_results + self.page_size - 1) // self.page_size
        results = self.get_page_info(1)["items"]
        
        search_info = {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }
        
        return search_info
    
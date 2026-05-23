class PageUtil:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size

    def get_page(self, page_number):
        start_index = (page_number - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def get_page_info(self, page_number):
        current_page = page_number
        per_page = self.page_size
        total_pages = self.total_pages
        total_items = self.total_items
        has_previous = current_page > 1
        has_next = current_page < total_pages
        data = self.get_page(current_page)
        return {
            "current_page": current_page,
            "per_page": per_page,
            "total_pages": total_pages,
            "total_items": total_items,
            "has_previous": has_previous,
            "has_next": has_next,
            "data": data
        }

    def search(self, keyword):
        results = [item for item in self.data if keyword in str(item)]
        total_results = len(results)
        total_pages = (total_results + self.page_size - 1) // self.page_size
        return {
            "keyword": keyword,
            "total_results": total_results,
            "total_pages": total_pages,
            "results": results
        }


Now, let's test our implementation.


page_util = PageUtil([1, 2, 3, 4], 1)
print(page_util.get_page(1))  # [1]
print(page_util.get_page_info(1))  # {'current_page': 1, 'per_page': 1, 'total_pages': 4, 'total_items': 4, 'has_previous': False, 'has_next': True, 'data': [1]}
print(page_util.search("1"))  # {'keyword': '1', 'total_results': 1, 'total_pages': 1,'results': [1]}
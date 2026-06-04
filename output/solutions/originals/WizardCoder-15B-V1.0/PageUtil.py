Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class PageUtil in the following code.
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

### Response:The class `PageUtil` is a versatile utility for handling pagination and search functionalities in an efficient and convenient manner. It has the following methods:

- `__init__(self, data, page_size)`: Initializes the `PageUtil` object with the given data and page size.
- `get_page(self, page_number)`: Retrieves a specific page of data.
- `get_page_info(self, page_number)`: Retrieves information about a specific page.
- `search(self, keyword)`: Searches for items in the data that contain the given keyword.

Let's implement each of these methods one by one.

### `__init__(self, data, page_size)`

The `__init__` method initializes the `PageUtil` object with the given data and page size. It sets the `data`, `page_size`, `total_items`, and `total_pages` attributes.

```python
class PageUtil:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.total_items = len(data)
        self.total_pages = (self.total_items + page_size - 1) // page_size
```

### `get_page(self, page_number)`

The `get_page` method retrieves a specific page of data. It returns a slice of the `data` attribute, starting from the `page_number` index and with a length of `page_size`.

```python
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
```

### `get_page_info(self, page_number)`

The `get_page_info` method retrieves information about a specific page. It returns a dictionary containing information about the current page, total pages, and whether there are previous or next pages. It also includes the `data` attribute for the current page.

```python
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
```

### `search(self, keyword)`

The `search` method searches for items in the data that contain the given keyword. It returns a dictionary containing information about the search results, including the total results, total pages, and matching items.

```python
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
```

Now, let's test our implementation.

```python
page_util = PageUtil([1, 2, 3, 4], 1)
print(page_util.get_page(1))  # [1]
print(page_util.get_page_info(1))  # {'current_page': 1, 'per_page': 1, 'total_pages': 4, 'total_items': 4, 'has_previous': False, 'has_next': True, 'data': [1]}
print(page_util.search("1"))  # {'keyword': '1', 'total_results': 1, 'total_pages': 1,'results': [1]}
```


class URLHandler:
    """
    The class supports to handle URLs, including extracting the scheme, host, path, query parameters, and fragment.
    """

    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url

    def get_scheme(self):
        """
        get the scheme of the URL
        :return: string, If successful, return the scheme of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_scheme()
        "https"
        """


    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """


    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """


    def get_query_params(self):
        """
        Get the request parameters for the URL
        :return: dict, If successful, return the request parameters of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """


    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """


    def get_url(self):
        """
        Get the URL of the URLHandler
        :return: string, If successful, return the URL of the URLHandler
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url()
        "https://www.baidu.com/s?wd=aaa&rsv_spt=1#page"
        """


    def get_url_handler(self):
        """
        Get the URLHandler of the URL
        :return: URLHandler, If successful, return the URLHandler of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url_handler()
        URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        """


    def get_url_handler_params(self):
        """
        Get the URLHandler's parameters
        :return: dict, If successful, return the URLHandler's parameters
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url_handler_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """


    def get_url_handler_fragment(self):
        """
        Get the URLHandler's fragment
        :return: string, If successful, return the URLHandler's fragment
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url_handler_fragment()
        "page"
        """


    def get_url_handler_query_params(self):
        """
        Get the URLHandler's query parameters
        :return: dict, If successful, return the URLHandler's query parameters
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url_handler_query_params()
        {"wd": "aaa", "rsv_spt": "1"}
        """


    def get_url_handler_query_params_with_params(self):
        """
        Get the URLHandler's query parameters with the parameters
        :return: dict, If successful, return the URLHandler's query parameters with the parameters
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url_handler_query_params_with_params()
        {"wd": "aaa", "rsv_spt": "1", "page": "page"}
        """


    def get_url_handler_query_params_with_params_and_fragment(self):
        """
        Get the URLHandler's query parameters with the parameters and fragment
        :return: dict, If successful, return the URLHandler's query parameters with the parameters and fragment
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_url_handler_query_params_with_params_and_fragment()
        {"wd": "aaa", "rsv_spt": "1", "page": "page", "page2": "page2"}
        """


    def get_url_handler_query_params_with_params_and_fragment_and_query_params(self):
        """
        Get the URLHandler's query parameters with the parameters and fragment and query parameters
        :return: dict, If successful, return the URLHandler's query parameters with the parameters and
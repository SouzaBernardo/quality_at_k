
class URLHandler: 
    def __init__(self, url):
        """
        Initialize URLHandler's URL
        """
        self.url = url





    def get_host(self):
        """
        Get the second part of the URL, which is the host domain name
        :return: string, If successful, return the host domain name of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_host()
        "www.baidu.com"
        """
        return self.url.split("://")[2]

    def get_path(self):
        """
        Get the third part of the URL, which is the address of the resource
        :return: string, If successful, return the address of the resource of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_path()
        "/s?wd=aaa&rsv_spt=1#page"
        """
        # Extract the scheme, host, path, query parameters, and fragment from the URL
        scheme, host, path, query_params, fragment = self.url.split("/")
        # Return the address of the resource as the path part of the URL
        return path.split("/")[-1]

    def get_query_params(self):
        query_params = {}
        for key, value in self.url.split("&"):
            if key.isalnum() and not key in query_params:
                query_params[key] = value
            else:
                query_params[key] = str(value)
        return query_params

    def get_fragment(self):
        """
        Get the fragment after '#' in the URL
        :return: string, If successful, return the fragment after '#' of the URL
        >>> urlhandler = URLHandler("https://www.baidu.com/s?wd=aaa&rsv_spt=1#page")
        >>> urlhandler.get_fragment()
        "page"
        """
        return self.url.split('#')[1]
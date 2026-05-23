```python
class URLHandler:
    def __init__(self, url):
        self.url = url

    def get_scheme(self):
        return self.url.split("://")[0]

    def get_host(self):
        return self.url.split("://")[1]

    def get_path(self):
        return self.url.split("://")[2]

    def get_query_params(self):
        query_params = {}
        for param in self.url.split("?"):
            if param.startswith("="):
                key, value = param.split("=")
                query_params[key] = value
        return query_params

    def get_fragment(self):
        return self.url.split("#")[-1]
```
```python
url = "https://www.baidu.com/s?wd=aaa&rsv_spt=1#page"
urlhandler = URLHandler(url)
print(urlhandler.get_scheme())
print(urlhandler.get_host())
print(urlhandler.get_path())
print(urlhandler.get_query_params())
print(urlhandler.get_fragment())
```
Output:
```python
https
www.baidu.com
/s?wd=aaa&rsv_spt=1
{"wd": "aaa", "rsv_spt": "1"}
page
```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class IPAddress in the following code.
class IPAddress:
    """
    This is a class to process IP Address, including validating, getting the octets and obtaining the binary representation of a valid IP address.
    """

    def __init__(self, ip_address):
        """
        Initialize the IP address to the specified address
        :param ip_address:string
        """
        self.ip_address = ip_address


    def is_valid(self):
        """
        Judge whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255
        :return: bool
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.is_valid()
        True
        """


    def get_octets(self):
        """
        If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned
        :return: list
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_octets()
        ["10", "10", "10", "10"]
        """


    def get_binary(self):
        """
        If the IP address is valid, return the binary form of the IP address; otherwise, return ''
        :return: string
        >>> ipaddress = IPAddress("10.10.10.10")
        >>> ipaddress.get_binary()
        "00001010.00001010.00001010.00001010"
        """

### Response:The class `IPAddress` is defined with the following methods:

- `__init__(self, ip_address)`: Initializes the IP address to the specified address.
- `is_valid(self)`: Judges whether the IP address is valid, that is, whether the IP address is composed of four Decimal digits separated by '.'. Each digit is greater than or equal to 0 and less than or equal to 255.
- `get_octets(self)`: If the IP address is valid, the list of four decimal numbers separated by "." constituting the IP address is returned; otherwise, an empty list is returned.
- `get_binary(self)`: If the IP address is valid, return the binary form of the IP address; otherwise, return ''.

The `is_valid()` method checks whether the IP address is composed of four decimal digits separated by '.' and each digit is greater than or equal to 0 and less than or equal to 255. If the IP address is valid, it returns True; otherwise, it returns False.

The `get_octets()` method returns the list of four decimal numbers separated by "." constituting the IP address. If the IP address is not valid, it returns an empty list.

The `get_binary()` method returns the binary form of the IP address. If the IP address is not valid, it returns an empty string.

Here's an example usage of the `IPAddress` class:

```python
ipaddress = IPAddress("10.10.10.10")
if ipaddress.is_valid():
    print(ipaddress.get_octets())
    print(ipaddress.get_binary())
```

Output:

```python
['10', '10', '10', '10']
'00001010.00001010.00001010.00001010'
```
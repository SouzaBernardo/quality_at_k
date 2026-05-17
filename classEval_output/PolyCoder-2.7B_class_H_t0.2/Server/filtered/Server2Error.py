class Server:
    """
    This is a class as a server, which handles a white list, message sending and receiving, and information display.
    """


    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}



    def add_white_list(self, addr):
        """
        Add an address to the whitelist and do nothing if it already exists
        :param addr: int, address to be added
        :return: new whitelist, return False if the address already exists
        >>> server = Server()
        >>> server.add_white_list(88)
        [88]
        """

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        abc
        """

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """

    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be'send' or'receive'
        :return: if type is equal to'send' or'receive', return the corresponding struct; otherwise, return False
        >>> server.recv({"addr":88,"content":"abc"})
        >>> server.send({"addr":66,"content":"ABC"})
        >>> server.show("send")
        {"addr":66,"content":"ABC"}
        """

    def get_white_list(self):
        """
        Return the list of whitelisted addresses
        :return: list of whitelisted addresses
        >>> server.get_white_list()
        [88]
        """

    def get_white_list_size(self):
        """
        Return the number of whitelisted addresses
        :return: the number of whitelisted addresses
        >>> server.get_white_list_size()
        0
        """

    def get_white_list_size_with_info(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_size_with_info()
        0
        """

    def get_white_list_with_info(self):
        """
        Return the list of whitelisted addresses and information
        :return: list of whitelisted addresses and information
        >>> server.get_white_list_with_info()
        [88]
        """

    def get_white_list_with_info_size(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_with_info_size()
        0
        """

    def get_white_list_with_info_size_with_info(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_with_info_size_with_info()
        0
        """

    def get_white_list_with_info_size_with_info_and_info(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_with_info_size_with_info_and_info()
        0
        """

    def get_white_list_with_info_size_with_info_and_info_and_info(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_with_info_size_with_info_and_info_and_info()
        0
        """

    def get_white_list_with_info_size_with_info_and_info_and_info_and_info(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_with_info_size_with_info_and_info_and_info_and_info()
        0
        """

    def get_white_list_with_info_size_with_info_and_info_and_info_and_info_and_info(self):
        """
        Return the number of whitelisted addresses and information
        :return: the number of whitelisted addresses and information
        >>> server.get_white_list_with_info_size_with_info_and_info_and_info_and_info_and_info()
        0
        """

    def get_white_list_with_info_size
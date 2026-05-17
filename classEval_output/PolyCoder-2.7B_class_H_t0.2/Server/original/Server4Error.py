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

    def send_struct(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        >>> server.send_struct({"addr":66,"content":"ABC"})
        self.send_struct = {"addr":66,"content":"ABC"}
        """

    def receive_struct(self, info):
        """
        Receive information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return nothing; otherwise, return a string indicating an error message
        >>> server.send_struct({"addr":66,"content":"ABC"})
        self.receive_struct = {"addr":66,"content":"ABC"}
        """


    def add_send_struct(self, addr, content):
        """
        Add an address and content to the sending list
        :param addr: int, address to be added
        :param content: str, content to be added
        :return: new sending list, return False if the address already exists
        >>> server.add_send_struct(88, "ABC")
        [88]
        """

    def del_send_struct(self, addr, content):
        """
        Remove an address and content from the sending list
        :param addr: int, address to be deleted
        :param content: str, content to be deleted
        :return: new sending list, return False if the address does not exist
        >>> server.add_send_struct(88, "ABC")
        >>> server.del_send_struct(88, "ABC")
        []
        """

    def add_receive_struct(self, addr, content):
        """
        Add an address and content to the receiving list
        :param addr: int, address to be added
        :param content: str, content to be added
        :return: new receiving list, return False if the address already exists
        >>> server.add_receive_struct(88, "ABC")
        [88]
        """

    def del_receive_struct(self, addr, content):
        """
        Remove an address and content from the receiving list
        :param addr: int, address to be deleted
        :param content: str, content to be deleted
        :return: new receiving list, return False if the address does not exist
        >>> server.add_receive_struct(88, "ABC")
        >>> server.del_receive_struct(88, "ABC")
        []
        """


    def add_white_list(self, addr):
        """
        Add an address to the white list
        :param addr: int, address to be added
        :return: new white list, return False if the address already exists
        >>> server.add_white_list(88)
        [88]
        """

    def del_white_list(self, addr):
        """
        Remove an address from the white list
        :param addr: int, address to be deleted
        :return: new white list, return False if the address does not exist
        >>> server.add_white_list(88)
        >>> server.del_white_list(88)
        []
        """


    def add_send_struct_
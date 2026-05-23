class Server: 
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
        """
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return self.white_list



    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        """
        addr = info["addr"]
        content = info["content"]
        if addr in self.white_list:
            self.receive_struct[addr] = content
            return content
        else:
            return False

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        """
        if "addr" not in info or "content" not in info:
            return "Invalid information format"
        if info["addr"] not in self.white_list:
            return "Address not in white list"
        self.send_struct = info

    def show(self, type):
        """
        Returns struct of the specified type
        :param type: string, the type of struct to be returned, which can be'send' or'receive'
        :return: if type is equal to'send' or'receive', return the corresponding struct; otherwise, return False
        """
        if type =='send':
            return self.send_struct
        elif type =='receive':
            return self.receive_struct
        else:
            return False
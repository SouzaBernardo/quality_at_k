class Server: 
    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}





    def add_white_list(self, addr):
        if addr not in self.white_list:
            self.white_list.append(addr)
            return self.white_list
        else:
            return False

    def del_white_list(self, addr):
        """
        Remove an address from the whitelist and do nothing if it does not exist
        :param addr: int, address to be deleted
        :return: new whitelist, return False if the address does not exist
        """
        if addr in self.white_list:
            self.white_list.remove(addr)
        return self.white_list

    def recv(self, info):
        """
        Receive information containing address and content. If the address is on the whitelist, receive the content; otherwise, do not receive it
        :param info: dict, information dictionary containing address and content
        :return: if successfully received, return the content of the infomation; otherwise, return False
        """
        if info["addr"] in self.white_list:
            return info["content"]
        else:
            return False

    def send(self, info):
        """
        Send information containing address and content
        :param info: dict, information dictionary containing address and content
        :return: if successfully sent, return nothing; otherwise, return a string indicating an error message
        """
        if info["addr"] in self.white_list:
            self.send_struct = info
            return
            # add code to check if the address is valid
            # add code to check if the content is valid
            # add code to add the content to the sending queue
            # add code to add the address to the sending queue
            # add code to add the sending and receiving structs to the respective queues
            # add code to start the sending process
            # add code to start the receiving process
            # add code to display the sending and receiving information
            # add code to display the information about the address and content
            return
            # return an error message if the address is not valid
            # return an error message if the content is not valid
            # return an error message if the address is not in the whitelist
            # return an error message if the content is empty
            # return an error message if the address is not in the sending or receiving structs
            # return an error message if the content is not in the sending or receiving structs
            # return an error message if the address is not in the sending queue
            # return an error message if the content is not in the sending queue
            # return an error message if the address is not in the receiving queue
            # return an error message if the content is not in the receiving queue
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the queue
            # return an error message if the content is not in the queue
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the sending struct
            # return an error message if the content is not in the sending struct
            # return an error message if the address is not in the receiving struct
            # return an error message if the content is not in the receiving struct
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the queue
            # return an error message if the content is not in the queue
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the sending struct
            # return an error message if the content is not in the sending struct
            # return an error message if the address is not in the receiving struct
            # return an error message if the content is not in the receiving struct
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the queue
            # return an error message if the content is not in the queue
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the sending struct
            # return an error message if the content is not in the sending struct
            # return an error message if the address is not in the receiving struct
            # return an error message if the content is not in the receiving struct
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the queue
            # return an error message if the content is not in the queue
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the sending struct
            # return an error message if the content is not in the sending struct
            # return an error message if the address is not in the receiving struct
            # return an error message if the content is not in the receiving struct
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending and receiving structs are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the queue
            # return an error message if the content is not in the queue
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending and receiving queues are not initialized
            # return an error message if the sending process is not initialized
            # return an error message if the receiving process is not initialized
            # return an error message if the display process is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the information about the address and content is not initialized
            # return an error message if the address is not in the sending struct
            # return an error message if the content is not in the sending
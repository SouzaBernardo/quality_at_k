class Server: 
    def __init__(self):
        """
        Initialize the whitelist as an empty list, and initialize the sending and receiving information as an empty dictionary
        """
        self.white_list = []
        self.send_struct = {}
        self.receive_struct = {}





    def add_white_list(self, addr):
        
        if addr in self.white_list:
            return False
        else:
            self.white_list.append(addr)
            return self.white_list


    def del_white_list(self, addr):
        

        if addr in self.white_list:
            self.white_list.remove(addr)
            return self.white_list
        else:
            return False


    def recv(self, info):
        
        if info["addr"] in self.white_list:
            return info["content"]
        else:
            return False





    def show(self, type):
        
        if type == "send":
            return self.send_struct
        elif type == "receive":
            return self.receive_struct
        else:
            return False

class Variable:
    def __init__(self, id : str,size : int):
        self.__offset = None
        self.size = size
        self.id = id

    def set_offset(self, offset : int):
        self.__offset = offset

    def get_offset(self):
        return self.__offset



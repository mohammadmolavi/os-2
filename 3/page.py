from variable import Variable

MAX_PAGE_SIZE = 400
class Page:
    def __init__(self, page_number : int, variable_list : list):
        self.is_present = False
        self.page_number = page_number
        self.__variable_list = variable_list
        self.memory_address : int

    def get_var (self, var_id : str) -> Variable:
        for var in self.__variable_list:
            if var.id == var_id:
                return var
from variable import Variable

MAX_PAGE_SIZE = 400
class Page:
    def __init__(self, page_number : int, variable_list : list):
        self.is_present = False
        self.page_number = page_number
        self.variable_list = variable_list
        self.memory_address = None

    def get_var (self, var_id : str) -> Variable:
        for var in self.variable_list:
            if var.id == var_id:
                return var
    def has_var(self, var_id : str):
        for var in self.variable_list:
            if var.id == var_id:
                return var

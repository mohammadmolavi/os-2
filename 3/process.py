from page import Page

MAX_PAGE_SIZE = 400

class Process:

    def __init__(self, variable_dic : dict):
        self.page_list = []
        self.variable_dic = variable_dic
        self.pagination(variable_dic)


    def get_containing_page(self):
        pass

    def pagination(self, var_size_dic : dict):
        cur_page_cap = 0
        for var_id, var_size in var_size_dic.items():
            if cur_page_cap + var_size <= MAX_PAGE_SIZE:
                cur_page_cap += var_size
            else:
                self.page_list.append(Page())
                cur_page_cap = 0

        if not cur_page_cap:
            self.page_list.append(Page())




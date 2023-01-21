from page import Page, MAX_PAGE_SIZE
from variable import Variable

class Process:

    def __init__(self, var_size_dic : dict):
        self.var_list = []
        offset = 0
        for var_id, var_size in var_size_dic.items():
            self.var_list.append(Variable(var_id, var_size, offset))
            offset += var_size
        self.page_list = []
        self.pagination(self.var_list)

    def get_page_of_var(self, var_id):
        for page in self.page_list:
            if page.has_var(var_id):
                return page

    def pagination(self, var_list : list):
        cur_page_cap = 0
        cur_page_vars = []
        page_number = 0
        for var in var_list:
            if cur_page_cap + var.size <= MAX_PAGE_SIZE:
                cur_page_cap += var.size
                cur_page_vars.append(var)
            else:
                self.page_list.append(Page(page_number, var_list))
                page_number += 1
                cur_page_cap = 0

        if not cur_page_cap:
            self.page_list.append(Page(page_number, var_list))
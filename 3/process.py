from page import Page, MAX_PAGE_SIZE
from variable import Variable

class Process:

    def __init__(self, var_size_dic : dict):
        self.var_list = []
        for var_id, var_size in var_size_dic.items():
            self.var_list.append(Variable(var_id, var_size))

        self.page_list = []
        self.pagination(self.var_list)

    def get_page_of_var(self, var_id):
        page : Page
        for page in self.page_list:
            if page.has_var(var_id):
                return page #todo

    def pagination(self, var_list : list):
        used_amount = 0
        cur_page_vars = []
        page_number = 0

        var : Variable
        for var in var_list:
            if used_amount + var.size <= MAX_PAGE_SIZE:
                var.set_offset(used_amount)
                used_amount += var.size

            else:
                self.page_list.append(Page(page_number, cur_page_vars))
                page_number += 1
                cur_page_vars = []
                var.set_offset(0)
                used_amount = var.size

            cur_page_vars.append(var)


        if used_amount > 0:
            self.page_list.append(Page(page_number, cur_page_vars))
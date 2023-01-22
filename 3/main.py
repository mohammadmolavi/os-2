from page import Page
from process import Process
from variable import Variable
from memory import Memory

INPUT_FILE = './testcase1.txt'
main_memory = Memory(400)
process_dic = {}

def main():
    file = open(INPUT_FILE, 'r')
    take_inputs(file)

    #recv requests
    input_line = file.readline().split()
    while input_line:
        print(input_line)
        proc_id = input_line[0]
        var_id = input_line[1]
        response(proc_id, var_id)
        input_line = file.readline().split()

def take_inputs(file):
    input_line = file.readline().split()
    process_count = int(input_line[0])

    for _ in range(process_count):
        input_line = file.readline().split()
        process_name = input_line[0]
        var_count = int(input_line[1])
        var_size_dic = {}
        for var in range(var_count):
            input_line = file.readline().split()
            print(input_line)
            var_size_dic[input_line[0]] = int(input_line[1])

        proc = Process(var_size_dic)
        process_dic[process_name] = proc


def response(proc_id, var_id):
    tar_proc: Process = process_dic.get(proc_id)
    if not tar_proc:
        print('proc not found')
        return

    tar_page: Page = tar_proc.get_page_of_var(var_id)
    if not tar_page:
        print('page not found')
        return

    tar_var: Variable = tar_page.get_var(var_id)
    if not tar_var:
        print('variable not found')
        return

    if not tar_page.is_present:
        tar_page.memory_address = main_memory.allocate(tar_page)

    print('Logical: Page {} offset {}'.format(tar_page.page_number, tar_var.get_offset()))
    print('Physical: frame {} offset {}'.format(tar_page.memory_address, tar_var.get_offset()))
    print('relative: {}'.format(tar_page.page_number * 400 + tar_var.get_offset()))

if __name__ == '__main__':
    main()
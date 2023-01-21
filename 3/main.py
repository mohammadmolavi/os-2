from page import Page
from process import Process
from variable import Variable

INPUT_FILE = './testcase1.txt'

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
        input_line = file.readline().split()
        tar_proc : Process = process_dic.get(proc_id)
        tar_page : Page = tar_proc.get_page_of_var(var_id)
        tar_var : Variable = tar_page.get_var(var_id)
        if not tar_var:
            print('err')

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

if __name__ == '__main__':
    main()
from process import Process
INPUT_FILE = './testcase1.txt'

def main():
    file = open(INPUT_FILE, 'r')

    input_line = file.readline().split()
    process_count = int(input_line[0])


    for _ in range(process_count):
        input_line = file.readline().split()
        process_name = input_line[0]
        var_count = int(input_line[1])
        var_dic = {}
        for var in range(var_count):
            input_line = file.readline().split()
            print(input_line)
            var_dic[input_line[0]] = int(input_line[1])

        process_dic = {}
        proc = Process(var_dic)
        process_dic[process_name] = proc
        print()
    #recv requests
    input_line = file.readline().split()
    while(input_line):
        print(input_line)
        input_line = file.readline().split()


if __name__ == '__main__':
    main()
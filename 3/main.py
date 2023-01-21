
INPUT_FILE = './testcase1.txt'
def main():
    file = open(INPUT_FILE, 'r')
    cmd_args = file.readline().split()
    while cmd_args:
        print(cmd_args)
        cmd_args = file.readline().split()



if __name__ == '__main__':
    main()
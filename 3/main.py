from process import process
INPUT_FILE = './testcase1.txt'
def main():

    file = open(INPUT_FILE, 'r')

    cmd_args = file.readline().split()
    processCount = cmd_args


    for process in processCount:
        cmd_args = file.readline().split()
        processName = cmd_args[0]
        varCount = int(cmd_args[1])
        varDic = {}
        for var in range(varCount):
            cmd_args = file.readline().split()
            print(cmd_args)
            varDic[cmd_args[0]] = int(cmd_args[1])

        processDic = {}
        proc = process(varDic)
        processDic[processName] = proc

    #recv requests
    cmd_args = file.readline().split()
    while(cmd_args):
        print(cmd_args)
        cmd_args = file.readline().split()


if __name__ == '__main__':
    main()
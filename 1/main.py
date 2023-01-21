import enum
from multiprocessing import Value, Array, Queue,Process
from time import sleep

class PID(enum.Enum):
    add = 0
    sub = 1
    mul = 2
    div = 3

class Locker:
    def __init__(self):
        self.queue = Queue(maxsize=1)

    def lock(self, pid : PID):
        self.queue.put(pid)

    def unlock(self, pid : PID):
        q_id = self.queue.get(False)
        if q_id != pid:
            raise Exception('not equal with whats in queue')

def add(num, value):
    tmp = 0
    while True:
        locker.lock(PID.add)
        print('add', value)
        num.value += value
        tmp = num.value
        sleep(1)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(PID.add)


def sub(num, value):
    tmp = 0
    while True:
        locker.lock(PID.sub)
        print('sub', value)
        num.value -= value
        tmp = num.value
        sleep(1.5)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(PID.sub)

def mul(num, value):
    tmp = 0
    while True:
        locker.lock(PID.mul)
        print('mul', value)
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(PID.mul)

def div(num, value):
    tmp = 0
    while True:
        locker.lock(PID.div)
        print('div', value)
        num.value /= value
        tmp = num.value
        sleep(3)
        if tmp != num.value:
            print("Process conflict")
        locker.unlock(PID.div)


def Show(num):
    while True:
        sleep(0.5)
        print(num.value)



if __name__ == '__main__':
    global_num = Value('d', 0.0)
    locker = Locker()
    p1 = Process(target=add, args=(global_num, 10))
    p2 = Process(target=sub, args=(global_num, 5))
    p3 = Process(target=add, args=(global_num, 2))
    p4 = Process(target=sub, args=(global_num, 4))

    show = Process(target=Show, args=(global_num,))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()

import enum
from multiprocessing import Process, Value, Array, Queue
from time import sleep


class LockOwner(enum.Enum):
    none = 'none'
    add = 'add'
    sub = 'sub'
    mul = 'mul'
    div = 'div'


class ProtectedValue:
    def __init__(self, value):
        self.__value = value
        self.__lock = LockOwner.none

    def get_lock(self, lock_owner):
        while self.__lock != LockOwner.none:
            pass
        lock = lock_owner
        return

    def get_value(self):
        return self.__value

    def set_value(self, lock_owner):
        if self.__lock == lock_owner:
            return self.__value

    def release_lock(self, lock_owner):
        if self.__lock == lock_owner:
            self.__lock = LockOwner.none
        else:
            return


def add(protected_num : ProtectedValue, const):
    tmp = 0
    while True:
        const.get_lock(LockOwner.add)
        print(LockOwner.add)
        protected_num.set_value(protected_num.get_value() + const)
        tmp = protected_num.get_value()
        sleep(1)
        if tmp != protected_num.get_value():
            print("Process conflict")
        const.release_lock(LockOwner.add)


def sub(protected_num : ProtectedValue, const):
    tmp = 0
    while True:
        protected_num.get_lock(LockOwner.sub)
        print(LockOwner.sub)
        protected_num.set_value(protected_num.get_value() - const)
        tmp = protected_num.value
        sleep(1.5)
        if tmp != protected_num.value:
            print("Process conflict")
        const.release_lock(LockOwner.sub)


def mul(num, value):
    tmp = 0
    while True:
        value.get_lock(LockOwner.mul)
        print('mul')
        num.value *= value
        tmp = num.value
        sleep(2)
        if tmp != num.value:
            print("Process conflict")
        value.release_lock(LockOwner.mul)


def div(num, value):
    tmp = 0
    while True:
        num.get_lock(LockOwner.div)
        print('div')
        num.value /= value
        tmp = num.value
        sleep(3)
        if tmp != num.value:
            print("Process conflict")
        num.release_lock(LockOwner.div)


def Show(num):
    while True:
        sleep(0.5)
        print(num.value)


if __name__ == '__main__':
    num = ProtectedValue(0.0)
    p1 = Process(target=add, args=(num, 10))
    p2 = Process(target=sub, args=(num, 5))
    p3 = Process(target=add, args=(num, 2))
    p4 = Process(target=sub, args=(num, 4))

    show = Process(target=Show, args=(num,))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()

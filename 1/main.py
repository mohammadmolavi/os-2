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
        self.__lock = lock_owner
        return

    def get_value(self):
        return self.__value

    def set_value(self, newValue):
        self.__value = newValue
        return self.__value

    def release_lock(self, lock_owner):
        if self.__lock == lock_owner:
            self.__lock = LockOwner.none
        else:
            return


def add(protected_num : ProtectedValue, const):
    tmp = 0
    while True:
        protected_num.get_lock(LockOwner.add)
        print(LockOwner.add)
        protected_num.set_value(protected_num.get_value() + const)
        tmp = protected_num.get_value()
        sleep(1)
        #print(tmp)
        if tmp != protected_num.get_value():
            print("Process conflict")
        protected_num.release_lock(LockOwner.add)


def sub(protected_num : ProtectedValue, const):
    tmp = 0
    while True:
        protected_num.get_lock(LockOwner.sub)
        print(LockOwner.sub)
        protected_num.set_value(protected_num.get_value() - const)
        tmp = protected_num.get_value()
        #print(tmp)
        sleep(1.5)
        if tmp != protected_num.get_value():
            print("Process conflict")
        protected_num.release_lock(LockOwner.sub)


def mul(protected_num : ProtectedValue, const):
    tmp = 0
    while True:
        protected_num.get_lock(LockOwner.mul)
        print(LockOwner.mul)
        protected_num.set_value(protected_num.get_value() * const)
        tmp = protected_num.get_value()
        #print(tmp)
        sleep(2)
        if tmp != protected_num.get_value():
            print("Process conflict")
        protected_num.release_lock(LockOwner.mul)


def div(protected_num : ProtectedValue, const):
    tmp = 0
    while True:
        protected_num.get_lock(LockOwner.div)
        print(LockOwner.div)
        protected_num.set_value(protected_num.get_value() / const)
        tmp = protected_num.get_value()
        #print(tmp)
        sleep(3)
        if tmp != protected_num.get_value():
            print("Process conflict")
        protected_num.release_lock(LockOwner.div)


def Show(num : ProtectedValue):
    while True:
        sleep(0.5)
        print(num.get_value())


if __name__ == '__main__':
    num = ProtectedValue(0.0)
    p1 = Process(target=add, args=(num, 10))
    p2 = Process(target=sub, args=(num, 5))
    p3 = Process(target=mul, args=(num, 2))
    p4 = Process(target=div, args=(num, 4))

    show = Process(target=Show, args=(num,))
    show.start()
    sleep(1)
    p1.start()
    p2.start()
    p3.start()
    p4.start()

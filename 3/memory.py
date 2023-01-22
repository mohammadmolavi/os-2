from page import Page,MAX_PAGE_SIZE
import time


class Memory:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.__storage = []
        for _ in range(int(self.memory_size / MAX_PAGE_SIZE)):
            self.__storage.append([True , None , None])


    def allocate(self , page: Page):
        create_time = float(time.time())
        flag = False

        for i in range(len(self.__storage)):
            if self.__storage[i][0]:
                flag = True
                break
        if not flag:
            self.FIFO_unallocate()

        for i in range(len(self.__storage)):
            if self.__storage[i][0]:
                self.__storage[i] = ([False, page, create_time])
                page.is_present = True
                return i

    def FIFO_unallocate(self):
        print('page f')
        oldest = 0
        for i in range(len(self.__storage)):
            if self.__storage[i][2] < self.__storage[oldest][2]:
                oldest = i
        self.__storage[oldest][0] = True


    def find_page(self , page: Page):
        for entry in self.__storage:
            if entry[1] == page:
                return self.__storage
        return -1
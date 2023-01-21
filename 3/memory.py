from page import Page
import time


class Memory:
    def __int__(self):
        self.momory_size = 4000
        self.__storage = []
        for _ in range(int(self.momory_size / 400)):
            self.__storage.append([True , Page() , 0.0])


    def allocate(self , page: Page):
        create_time = float(time.time())
        flag = False
        for entry in self.__storage:
            if entry[0] == False:
                entry=([False , page , create_time])
                flag = True
                break
        if not flag:
            self.FIFO_unallocate()
            self.allocate(page)


    def unallocate(self , page: Page):
        for i in range(int(self.momory_size/400)):
            if self.__storage[i][1] == page :
                self.__storage[i][0] = True


    def FIFO_unallocate(self):
        oldest = 0
        for i in range(len(self.__storage)):
            if self.__storage[i][2] < self.__storage[oldest][2]:
                oldest = i
        self.__storage[oldest][2] = True


    def find_page(self , page: Page):
        for entry in self.__storage:
            if entry[1] == page:
                return self.__storage
        return -1
from page import Page
import time

class Memory:
    def __int__(self):
        self.momory_size = 4000
        self.__storage = []
        for _ in range(int(self.momory_size / 400)): #todo
            self.__storage.append([True , Page() , 0.0])

    def allocate(self , page: Page):
        create_time = float(time.time())
        if self.momory_size >= 400:
            for entry in self.__storage:
                if entry[0] == False:
                    entry=([False , page , create_time])
                    break
        else:
            pass
            #(fault)

    def unallocate(self , page: Page):
        for i in range(int(self.momory_size/400)):
            if self.__storage[i][1] == page :
                self.__storage[i][0] = True

    def FIFO_unallocate(self):
        oldest = self.__storage[1]
        for page in self.__storage:
            if page[1] < oldest:
                self.__storage.remove(page)
                self.momory_size -= 400


    def find_page(self , page: Page):
        try:
            return self.__storage.index(page)
        except:
            return "this page isn't exist in memory"
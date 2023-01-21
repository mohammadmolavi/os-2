
from multiprocessing import  Process, Queue, Value,Array
from time import sleep
from Car import Car



def producer(queue, id,):
    print('Producer: Running', flush=True)
    while True:
        value = Car(id.value)
        id.value += 1
        sleep(0.5)
        queue.put(value)


def consumer(queue, street : Queue):
    print('Consumer: Running', flush=True)
    while True:
        item = queue.get()     
        street.put(item.id)
        print('car id: ', item.id, 'sleep: ', item.time)
        temp = item.id
        sleep(item.time)
        street.get()
        if temp != item.id:
            print('Process conflict!')
   


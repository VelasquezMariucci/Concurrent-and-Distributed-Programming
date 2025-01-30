import random
import threading
import time

numberList = []
threads = []
mutex = threading.Lock()

for i in range(10):
    numberList.append(random.randint(0, 10))

print(list(numberList))


def readNums():
    mutex.acquire()
    try:
        print(numberList[-1])
    finally:
        mutex.release()
        time.sleep(1)


def writeNums(num):
    mutex.acquire()
    try:
        numberList.append(num)
    finally:
        mutex.release()
        time.sleep(1)


writeThread = threading.Thread(target=writeNums, args=(random.randint(10, 20),))
readThread = threading.Thread(target=readNums, args=())

writeThread.start()
readThread.start()

writeThread.join()
readThread.join()

print(list(numberList))


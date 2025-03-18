import time
import random
from threading import Thread, current_thread

SIZE:int = 10
shared_memory:list = [-1] * SIZE

class RandomProducer(Thread):
    def run(self) -> None:
        self.name:str = "Random Producer"
        global shared_memory
        for i in range(SIZE):
            rand = random.randint(1, 100)
            print(f"{current_thread().name} -> writing {rand}")
            shared_memory[i] = rand

class ArrayMul(Thread):
    def run(self) -> None:
        self.name:str = "Array Multiplication"
        arr:list = [i * i for i in range(SIZE)]
        global shared_memory
        for i in range(SIZE):
            while True:
                line = shared_memory[i]
                if line == -1:
                    print(f"{current_thread().name} -> Data not available, sleeping for 1 sec ...")
                    time.sleep(1)
                    continue
                print(f"{current_thread().name} -> Multiplying {arr[i]} * {shared_memory[i]}")
                arr[i] = arr[i] * shared_memory[i]
                break
        print(f"The result array is {arr}")

if __name__ == '__main__':
    threads:list = [
        RandomProducer(),
        ArrayMul()
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
from multiprocessing import Process
import time,random
import os

class TestCourse(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print(os.getppid(), os.getpid())
        print('%s is piaoing' % self.name)
        # time.sleep(random.randint(1,3))
        print('%s is piao end' % self.name)

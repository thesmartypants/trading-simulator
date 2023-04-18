from myqueue import MyQueue
import math


class Manager:
    def __init__(self):
        self.variency = MyQueue(3)

    def check(self, avg, price, sd_mult):
        self.variency.add((price - avg) ** 2)
        if self.variency.is_ready():
            
            sd = sd_mult*math.sqrt(self.variency.get_avg())

            return avg+sd > price > avg-sd
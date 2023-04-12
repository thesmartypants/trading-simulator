from queue import Queue
import math


class Manager:
    def __init__(self):
        self.variency = Queue(3)

    def check(self, avg, price, sd_mult):
        if self.variency.is_ready():
            self.variency.add((price - avg) ** 2)
            
            sd = sd_mult*math.sqrt(self.variency.get_avg())
            
            return avg+sd > price > avg-sd
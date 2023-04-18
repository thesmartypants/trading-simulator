class MyQueue:

    def __init__(self, size):
        self.size = size
        self.arr = []

    def add(self, element):
        self.arr.append(element)
        if len(self.arr) > self.size:
            self.arr.remove(self.arr[0])

    def get_avg(self):
        if self.is_ready():
            return sum(self.arr) / self.size
        else:
            return 0  # todo: throw exception

    def print_content(self):
        print(self.arr)

    def is_ready(self):
        return len(self.arr) == self.size

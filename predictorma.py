from queue import Queue


class PredictorMa:
    def __init__(self):
        self.prices = Queue(3)
        self.cur_mov_avg=0

    def get_signal(self, new_price):
        self.prices.add(new_price)
        if self.prices.is_ready():
            self.cur_mov_avg = self.prices.get_avg()
            if self.cur_mov_avg > new_price:
                return 'buy'
            elif self.cur_mov_avg < new_price:
                return 'sell'
            else:
                return ''

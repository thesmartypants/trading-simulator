class AvgPredict:
    def __init__(self, history):
        self.history = history
        self.change_avg = 0

    def give_signal(self, price):
        self.history.append(price)
        self.change_avg = 0
        for i in range(len(self.history)):
            if i != 0:
                self.change_avg += self.history[i] - self.history[i - 1]

        self.change_avg = self.change_avg / len(self.history)
        if self.change_avg > 0:
            return 'sell'
        elif self.change_avg < 0:
            return 'buy'
        else:
            return ''

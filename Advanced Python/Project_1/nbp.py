
class ExRate:
    def __init__(self, curr, code, ask_rate, bid_rate):
        self.curr = curr
        self.code = code
        self.ask_rate = ask_rate
        self.bid_rate = bid_rate
    
    def __repr__(self):
        return f'({self.curr}{self.code}{self.ask_rate}{self.bid_rate})'



class ExRateTable:
    def __init__(self, name, eff_date, rates=None):
        self.name = name
        self.eff_date = eff_date
        if rates is None:
            self.rates = []
        else:
            self.rates = rates 
    

    def add_rate(self, x):
        self.rates.append(x)


    def get_rate(self, code):
        for x in self.rates:
            if x.code == code:
                return x

    def __getitem__(self, item):
        result = self.get_rate(item)
        if result is not None:
            return result
        else:
            raise KeyError(item)
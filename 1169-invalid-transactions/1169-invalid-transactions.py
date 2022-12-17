class Solution:
    def __init__(self):
        self.records = {}
        
    def populateRecords(self, transactions: List[str]) -> None:
        for t in transactions:
            name, time, amount, city = t.split(",")
            time = int(time)
            if time in self.records:
                if name in self.records[time]:
                    self.records[time][name].append(city)
                else:
                    self.records[time][name] = [city]
            else:
                self.records[time] = {name:[city]}
            
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        self.populateRecords(transactions)
        res = []
        for trans in transactions:
            name, time, amount, city = trans.split(",")
            time = int(time)
            if int(amount) > 1000:
                res.append(trans)
                continue

            for time in range(time - 60, time + 61):
                if time not in self.records:
                    continue
                if name not in self.records[time]:
                    continue
                if len(self.records[time][name]) > 1 or self.records[time][name][0] != city:
                    res.append(trans)
                    break

        return res

            
class Transaction:
    def __init__(self, name: str, time: int, amount: int, city: str):
        self.name = name
        self.time = time
        self.amount = amount
        self.city = city
    
    def isInvalid(self) -> bool:
        return self.amount > 1000
    
    @staticmethod
    def fromString(t):
        name, time, amount, city = t.split(",")
        time, amount = int(time), int(amount)
        return Transaction(name, time, amount, city)

    def __str__(self):
        return f"{self.name},{self.time},{self.amount},{self.city}"

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        history = defaultdict(dict)
        result = []

        transactionsObj = [Transaction.fromString(t) for t in transactions]

        for t in transactionsObj:
            name, time, amount, city = t.name, t.time, t.amount, t.city

            if name not in history[time]:
                history[time][name] = {city}
            else:
                history[time][name].add(city)

        for t in transactionsObj: 
            name, time, amount, city = t.name, t.time, t.amount, t.city

            if t.isInvalid():
                result.append(str(t))
                continue
            
            for invalidTime in range(t.time - 60, t.time + 61):
                if invalidTime not in history:
                    continue
                if name not in history[invalidTime]:
                    continue

                citySet = history[invalidTime][name]
                
                if city not in citySet or len(citySet) > 1:
                    result.append(str(t))
                    break
        
        return result

    def invalidTransactions2(self, transactions: List[str]) -> List[str]:
        history = defaultdict(dict)
        result = []

        for t in transactions:
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)

            if name not in history[time]:
                history[time][name] = {city}
            else:
                history[time][name].add(city)

        for t in transactions:
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)
            
            if amount > 1000:
                result.append(t)
                continue
            
            for invalidTime in range(time - 60, time + 61):
                if invalidTime not in history:
                    continue
                if name not in history[invalidTime]:
                    continue

                citySet = history[invalidTime][name]
                
                if city not in citySet or len(citySet) > 1:
                    result.append(t)
                    break

        return result


        
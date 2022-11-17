class Solution:               
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        trans = [x.split(',') for x in transactions]
        for i in range(len(trans)):
            name, time, money, location = trans[i]
            time = int(time)
            money = int(money)
            if money > 1000:
                res.append(transactions[i])
                continue
            for j in range(len(trans)):
                if i != j:
                    name1, time1, money1, location1 = trans[j]
                    time1=int(time1)
                    if name1 == name and abs(time1-time) <= 60 and location1 != location:
                        res.append(transactions[i])
                        break
        return res
        
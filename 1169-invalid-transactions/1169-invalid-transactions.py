class Solution: 
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactionMap = {}
        for trans in transactions:
            name, time, amount, city = trans.split(",")
            time = int(time)
            if time in transactionMap:
                if name in transactionMap[time]:
                    transactionMap[time][name].append(city)
                else:
                    transactionMap[time][name] = [city]
            else:
                transactionMap[time] = {name:[city]}
        
        invalidTrans = []
        for trans in transactions:
            name, time, amount, city = trans.split(",")
            if int(amount) > 1000:
                invalidTrans.append(trans)
                continue

            for time in range(int(time)-60, int(time)+61):
                if time not in transactionMap:
                    continue
                if name not in transactionMap[time]:
                    continue
                if len(transactionMap[time][name]) > 1 or transactionMap[time][name][0] != city:
                    invalidTrans.append(trans)
                    break

        return invalidTrans

            
class Solution:   
    class Transaction:
        def __init__(self, data):
            self.name = data[0]
            self.time = int(data[1])
            self.amount = int(data[2])
            self.city = data[3]
            
        def toString(self):
            return self.name + "," + str(self.time) + "," + str(self.amount) + "," +self.city
            
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transMap = {}
        res = []
        for transaction in transactions:
            currTrans = Solution.Transaction(transaction.split(","))
            if currTrans.name in transMap:
                transMap[currTrans.name].append(currTrans)
            else:
                transMap[currTrans.name] = [currTrans]

        for transaction in transactions:
            currTrans = Solution.Transaction(transaction.split(","))
            if currTrans.amount > 1000:
                res.append(currTrans.toString())
                continue
                
            if currTrans.name in transMap:
                for prevTrans in transMap[currTrans.name]:
                    if currTrans.city != prevTrans.city and abs(currTrans.time - prevTrans.time) <= 60:
                        res.append(currTrans.toString())
                        break
        return res
  
        
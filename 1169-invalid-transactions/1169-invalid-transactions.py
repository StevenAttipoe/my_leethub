class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
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


        
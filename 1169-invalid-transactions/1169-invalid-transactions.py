class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        graph = defaultdict(dict)

        for t in transactions:
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)

            if name in graph[time]:
                graph[time][name].add(city)
            else:
                graph[time][name] = {city}

        result = []
        for t in transactions:
            name, time, amount, city = t.split(",")
            time, amount = int(time), int(amount)

            if amount > 1000:
                result.append(t)
                continue
            
            for minute in range(time - 60, time + 61):
                if minute not in graph:
                    continue
                if name not in graph[minute]:
                    continue

                citySet = graph[minute][name]

                if city not in citySet or len(citySet) > 1:
                    result.append(t)
                    break
            
        return result
        
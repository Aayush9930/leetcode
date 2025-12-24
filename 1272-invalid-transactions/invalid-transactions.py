class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def str_parser(s, i):
            x = s.split(",")
            res = {
                "name": x[0],
                "time": int(x[1]),
                "amount": int(x[2]),
                "city": x[3],
                "index": i
            } 
            return res

        invalid_transactions = set()
        h = {}

        for i in range(len(transactions)):  
            x = str_parser(transactions[i], i)
            if x["amount"] > 1000:
                invalid_transactions.add(i)
            
            if x['name'] in h:
                h[x['name']].append((x['time'], x['city'], x['index']))
            else:
                h[x['name']] = [(x['time'], x['city'], x['index'])]

        for name in h:
            h[name].sort(key=lambda x: x[0]) 

        for name in h:
            for i in range(len(h[name])):
                t1, c1, i1 = h[name][i]
                for j in range(i + 1, len(h[name])):
                    t2, c2, i2 = h[name][j]
                    if abs(t2 -t1) <= 60 and c1 != c2:
                        invalid_transactions.add(i1)
                        invalid_transactions.add(i2)
                    elif abs(t2 -t1) > 60:
                        break
        out = []
        for i in invalid_transactions:
            out.append(transactions[i])
        
        return out
                        



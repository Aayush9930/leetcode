class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_set = set()
        h = {}

        def parse_string(s, i):
            x = s.split(',')
            x = {
                "index": i,
                "name": x[0],
                "time": int(x[1]),
                "amount": int(x[2]),
                "city": x[3]
            }
            return x
        
        for i, tran in enumerate(transactions):
            x = parse_string(tran, i)

            if x["amount"] > 1000:
                invalid_set.add(x['index'])
            
            if x["name"] in h:
                h[x["name"]].append(x)

            else:
                h[x["name"]] = [x]
        
        for name in h:
            h[name].sort(key=lambda tx: tx["time"])
        
        for name in h:
            for i in range(len(h[name])):
                for j in range(i + 1, len(h[name])):
                    if h[name][j]["time"] - h[name][i]["time"] <= 60:
                        if h[name][i]["city"] != h[name][j]["city"]:
                            invalid_set.add(h[name][i]['index'])
                            invalid_set.add(h[name][j]['index'])
                    
                    else:
                        break
        out = []
        for index in invalid_set:
            out.append(transactions[index])
        
        return out
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value,timestamp])


    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        n = len(values)
        l = 0
        h = n-1
        lower_value = -1
        while l <= h:
            m = (l+h)//2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] > timestamp:
                h = m-1
            else:
                lower_value = m 
                l = m+1
        if lower_value == -1:
            return ""
        return values[lower_value][0]


        

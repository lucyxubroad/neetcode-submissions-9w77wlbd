class TimeMap:

    def __init__(self):
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dictionary:
            self.dictionary[key].append((timestamp, value))
        else:
            self.dictionary[key] = [(timestamp, value)]
    
    def get(self, key: str, timestamp: int) -> str:
        key_dict = self.dictionary.get(key, [])
        values = sorted(key_dict)
        start, end = 0, len(values)-1
        res = ''
        while start <= end:
            mid = (end-start)//2+start
            (t, v) = values[mid]
            if t <= timestamp:
                res = v
                start = mid+1
            else:
                end = mid-1

        return res

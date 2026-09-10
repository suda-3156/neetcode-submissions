from collections import defaultdict


class TimeMap:
    def __init__(self):
        # key -> list of timestamps
        self.key_timestamp: dict[str, list[int]] = defaultdict(list)
        # key + str(timestamp) -> val
        self.keytime_val: dict[str, str] = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamp[key].append(timestamp)
        self.keytime_val[key + str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        times = self.key_timestamp[key]
        n = len(times)

        if n == 0 or timestamp < times[0]:
            return ""

        if times[-1] <= timestamp:
            return self.keytime_val[key + str(times[-1])]

        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2

            if times[mid] > timestamp:
                right = mid
            else:
                left = mid + 1

        return self.keytime_val[key + str(times[right - 1])]

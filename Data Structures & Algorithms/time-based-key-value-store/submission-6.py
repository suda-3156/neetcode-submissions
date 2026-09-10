from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.key_timestamps: dict[str, list[int]] = defaultdict(list) # strictly increasing
        self.key_time_val: dict[str, int] = {} # key+"timestamp" -> value

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamps[key].append(timestamp)
        self.key_time_val[key + str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if len(self.key_timestamps[key]) == 0:
            return ""

        timestamps = self.key_timestamps[key]
        if timestamps[0] > timestamp:
            return ""
        if timestamps[-1] <= timestamp:
            return self.key_time_val[key + str(timestamps[-1])]

        # find the largest timestamp_prev
        left, right = 0, len(timestamps)

        while left < right:
            mid = (left + right) // 2

            if timestamps[mid] >= timestamp:
                right = mid
            else:
                left = mid + 1
        
        timestamp_prev = timestamps[left]
        if timestamp_prev != timestamp and left > 0:
            timestamp_prev = timestamps[left - 1]

        return self.key_time_val[key + str(timestamp_prev)]
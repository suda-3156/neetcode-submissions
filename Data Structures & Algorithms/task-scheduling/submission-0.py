class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0 for _ in range(26)]
        for task in tasks:
            count[ord(task) - ord("A")] += 1

        max_heap = [n for n in count if n != 0]
        heapq.heapify_max(max_heap)

        time = 0
        queue = deque()  # pairs of [cnt, idle_time]
        while max_heap or queue:
            time += 1

            if not max_heap:
                time = queue[0][1]
            else:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt > 0:
                    queue.append([cnt, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush_max(max_heap, queue.popleft()[0])

        return time

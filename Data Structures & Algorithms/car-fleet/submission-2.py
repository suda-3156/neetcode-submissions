class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd: list[list[int]] = []
        for i in range(len(position)):
            pos_spd.append([position[i], speed[i]])

        # O(n log(n))
        pos_spd.sort(reverse=True, key=lambda x: x[0])

        goal_times = []
        for pos, spd in pos_spd:
            time = (target - pos) / spd

            if not goal_times:
                goal_times.append(time)
                continue

            if goal_times[-1] < time:
                goal_times.append(time)

        return len(goal_times)

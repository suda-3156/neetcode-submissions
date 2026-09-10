class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if self.canEatAll(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def canEatAll(self, piles: List[int], h: int, k: int) -> bool:
        took = 0

        for pile in piles:
            took += (pile + k - 1) // k

        return took <= h

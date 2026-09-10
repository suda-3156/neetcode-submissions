class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) # O(n)

        while left < right: # O(nlogn)
            mid = (left + right) // 2

            if self.canEatAll(piles, h, mid): # O(n)
                right = mid
            else:
                left = mid + 1
        
        return right

    def canEatAll(self, piles: List[int], h: int, k: int) -> bool:
        need = 0

        for pile in piles:
            need += (pile + k - 1) // k

        return need <= h
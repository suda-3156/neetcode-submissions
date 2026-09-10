class Solution:
    def getKth(self, A: list[int], B: list[int], k: int) -> int:
        if len(A) > len(B):
            A, B = B, A

        if len(A) == 0:
            return B[k - 1]

        if k == 1:
            return min(A[0], B[0])

        i = min(len(A), k // 2)
        j = min(len(B), k // 2)

        if A[i - 1] <= B[j - 1]:
            return self.getKth(A[i:], B, k - i)

        else:
            return self.getKth(A, B[j:], k - j)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return float(self.getKth(nums1, nums2, (total + 1) // 2))
        else:
            return (self.getKth(nums1, nums2, total // 2) + self.getKth(nums1, nums2, total // 2 + 1)) / 2.0
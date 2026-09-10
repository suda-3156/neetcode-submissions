from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # self.genKey(s) -> list of anagrams
        count_anagrams: dict[str, list[str]] = defaultdict(list)

        for s in strs:
            count_anagrams[self.genKey(s)].append(s)

        return list(count_anagrams.values())
        
        
    def genKey(self, s: str) -> str:
        count: list[int] = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1
             
        return ",".join(list(map(str, count)))
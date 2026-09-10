class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict[str, list of words]
        groups: dict[str, list[str]] = defaultdict(list)

        for w in strs:
            times_appeared: list[int] = [0] * 26

            for c in w:
                times_appeared[ord(c) - ord("a")] += 1

            # this key can be sorted word
            # key = list(w)
            # key.sort()
            # key = "".join(key)
            key = "-".join(list(map(str, times_appeared)))

            groups[key].append(w)

        ans: list[list[str]] = []
        for words in groups.values():
            ans.append(words)

        return ans

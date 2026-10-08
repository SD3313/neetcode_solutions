class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import defaultdict
        hashmap1, hashmap2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            hashmap1[s[i]] += 1
            hashmap2[t[i]] += 1
        return hashmap1 == hashmap2            

        
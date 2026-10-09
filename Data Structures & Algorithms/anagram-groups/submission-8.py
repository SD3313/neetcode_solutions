class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashres = {}
        for s in strs:
            hsh = {}
            for l in s:
                hsh[l] = hsh.get(l, 0) + 1
            klucz = frozenset(hsh.items())
            hashres.setdefault(klucz, []).append(s)
        return list(hashres.values())
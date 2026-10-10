class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hsh = {}
        for n in nums:
            hsh[n] = hsh.get(n,0) + 1


        res=[]

        buckets = [[] for _ in range(len(nums)+1)]
        for num,freq in hsh.items():
            buckets[freq].append(num)

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        # slownika ma postac:
        # litera : index w nums
        for i in range(len(nums)):
            c = target - nums[i] 
            if c in hash:
                return [hash[c],i]
            hash[nums[i]] = i
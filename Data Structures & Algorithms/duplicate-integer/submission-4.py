class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       setnums ={r for r in nums}
       return(len(nums)> len(setnums))

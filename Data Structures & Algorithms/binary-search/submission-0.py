class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        mid = (lower + upper) // 2
        while(True):
            mid = (lower + upper) // 2
            if nums[mid] == target:
                return mid
            if upper <= lower:
                return -1
            if target > nums[mid]:
                lower = mid + 1
            if target < nums[mid]:
                upper = mid - 1
        

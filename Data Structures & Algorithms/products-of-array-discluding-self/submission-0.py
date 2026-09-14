class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefs = [nums[0]]
        sufs = [nums[-1]]
        for i in range(1, len(nums)):
            prefs.append(prefs[-1] * nums[i])
        for i in range(len(nums) - 2, -1, -1):
            sufs.append(sufs[-1] * nums[i])

        output = [sufs[-2]]

        for i in range(1, len(nums) - 1):
            p = prefs[i - 1]
            s = sufs[len(nums) - i - 2]
            output.append(p * s)

        output.append(prefs[-2])
        return output
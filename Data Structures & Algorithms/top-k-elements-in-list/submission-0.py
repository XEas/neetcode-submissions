class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = [[] for _ in range(len(nums) + 1)]
        frq_map = {}
        for num in nums:
            if (num in frq_map):
                frq_map[num] += 1
            else:
                frq_map[num] = 1
        
        for key, value in frq_map.items():
            frq[value].append(key)
        
        i = 0
        j = 0
        frq = frq[::-1]
        out = []
        while i != k:
            for num in frq[j]:
               out.append(num)
               i += 1
               if i == k:
                    break
            j += 1
        return out 
                

        
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        # 求不同平均值的数目->求数组内最大值和最小值相加过后的数目
        res_list = set()
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            res_list.add(nums[i] + nums[j])
            i += 1
            j -= 1
        return len(res_list)


sol = Solution()
nums = [4,1,4,0,3,5]
print(sol.distinctAverages(nums))
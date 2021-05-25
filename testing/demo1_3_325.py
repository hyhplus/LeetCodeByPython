
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        s = 0
        d = {0: -1}
        res = 0

        for i in range(len(nums)):
            s += nums[i]
            if s - k in d:
                res = max(res, i-d[s-k])
            if s not in d:
                d[s] = i
        
        return res


class Solution1:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        dic = {0: -1}
        res = sdt = 0
        for i in range(len(nums)):
            sdt += nums[i]
            if sdt - k in dic:
                res = max(res, i-dic[sdt-k])
            if sdt not in dic:
                dic[sdt] = i
        return res


from collections import defaultdict

class Solution2:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum_idx = defaultdict(int)
        res = 0
        presum = 0
        presum_idx[0] = 0   # 前0个，和为0   也决定了必须用虚指
        for i in range(n):
            presum += nums[i]
            if presum not in presum_idx:
                presum_idx[presum] = i + 1
            if (presum - k) in presum_idx:
                res = max(res, i - presum_idx[presum - k] + 1)
        
        return res


s = Solution1()
a = s.maxSubArrayLen([1, 2, 3, 1, 0,8], 7)
print(a)

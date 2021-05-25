class Solution1:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n, maxp = len(piles), max(piles)
        sump = sum(piles)
        if n == h: return maxp
        left, right = (sump-1)//h+1, min(maxp, sump//(h-n))
        while left < right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += (pile-1)//mid+1
                if time > h: break
            if time > h:
                left = mid + 1
            else:
                right = mid
        return left


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sdt = 0
        ms = float("-inf")
        for c in piles:
            sdt += c
            if c > ms:
                ms = c
        nxt = len(piles)
        if nxt == h:
            return ms
        res = ceil(sdt / h)
        rst = min(ms,sdt//(h-nxt))
        while res < rst:
            mid = (res+rst)>>1
            if sum(ceil(p / mid) for p in piles) <= h:
                rst = mid
            else:
                res = mid + 1
        return res
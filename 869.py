class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def num_count(x):
            cnt = [0] * 10
            while x:
                cnt[x % 10] += 1
                x //= 10
            return tuple(cnt)
        
        all_cnt = {num_count(1<<i) for i in range(32)}
        return num_count(n) in all_cnt
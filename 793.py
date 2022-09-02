class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(x):
            cnt = 0
            while x > 0:
                x //= 5
                cnt += x
            return cnt

        def bis_left(tar):
            low = 0
            high = (tar+1) * 5  # 因为f(5k) >= k，所以可以使用5k作为上界，而5(k+1)是为了处理k=0时的情况

            while low < high:
                mid = (low + high) >> 1
                tmp = f(mid)
                if tmp < tar:
                    low = mid + 1
                else:
                    high = mid

            return low

        return bis_left(k+1) - bis_left(k)

package leetcode

var MOD = 1337

func superPow(a int, b []int) int {
	n := len(b)
	ans := 1
	for i := n - 1; i >= 0; i-- {
		ans = (ans % MOD) * (pow(a, b[i]) % MOD) % MOD
		a = pow(a, 10)
	}
	return ans
}

func pow(a, n int) int {
	ans := 1
	for ; n > 0; n /= 2 {
		if n&1 > 0 { // 二进制位为1
			ans = ans * a % MOD
		}
		a = a * a % MOD
	}
	return ans
}

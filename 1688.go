package leetcode

func numberOfMatches(n int) int {
	// ans := 0
	// for n > 1 {
	//     ans += n >> 1
	//     n = n >> 1 + n & 1
	// }
	// return ans
	// 配对一次即比赛一次淘汰一支队伍
	// 最后剩一支队伍即淘汰了(n-1)支队伍
	// 即比赛了(n-1)次即配对了(n-1)次
	return n - 1
}

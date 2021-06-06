package leetcode

func isPowerOfFour(n int) bool {
	// for n > 0 {
	//     if n == 1 {
	//         return true
	//     }
	//     if n & 3 > 0 {
	//         return false
	//     }
	//     n >>= 2
	// }
	// return false
	// return n>0 && n&(n-1)==0 && n&0xaaaaaaaa==0  //只有一个1并且在偶数位上
	return n > 0 && n&(n-1) == 0 && n&0x55555555 > 0
}

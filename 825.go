package leetcode

// func numFriendRequests(ages []int) int {
// 	ans := 0
// 	sort.Ints(ages)
// 	n := len(ages)
// 	for i := 0; i < n; i++ {
// 		l := sort.Search(n, func(k int) bool {
// 			return ages[k] > ages[i]/2+7
// 		})
// 		r := sort.Search(n, func(k int) bool {
// 			return ages[k] > ages[i]
// 		})
// 		if l >= r {
// 			continue
// 		}
// 		ans += r - l - 1
// 	}
// 	return ans
// }

func numFriendRequests(ages []int) int {
	ans := 0
	buckets := [121]int{}
	for _, val := range ages {
		buckets[val]++
	}
	pre := [121]int{}
	for i := 1; i < 121; i++ {
		pre[i] = pre[i-1] + buckets[i]
	}
	for age := 15; age < 121; age++ {
		ans += buckets[age] * (pre[age] - pre[age/2+7] - 1)
	}
	return ans
}

// func main() {
// 	ages := []int{20, 30, 100, 110, 120}
// 	fmt.Println(numFriendRequests(ages))
// }

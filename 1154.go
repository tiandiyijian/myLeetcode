package leetcode

import (
	"strconv"
	"strings"
)

var month_days = [12]int{31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365}

func dayOfYear(date string) int {
	date_arr := strings.Split(date, "-")
	year, _ := strconv.ParseInt(date_arr[0], 10, 32)
	month, _ := strconv.ParseInt(date_arr[1], 10, 32)
	day, _ := strconv.ParseInt(date_arr[2], 10, 32)
	if month == 1 {
		return int(day)
	}
	if month <= 2 {
		return int(day) + 31
	}
	ans := 0
	if (year%100 == 0 && year%400 == 0) || (year%4 == 0) {
		ans += 1
	}
	return ans + int(day) + month_days[month-2]
}

// func main() {
// 	fmt.Println(dayOfYear("2019-03-01"))
// }

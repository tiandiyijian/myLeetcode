package leetcode

func dayOfTheWeek(day int, month int, year int) string {
	days := 3
	days += (year - 1971) * 365
	days += (year - 1969) / 4 // 1972年是第一个闰年，2000年恰好是闰年，从1973年开始这项才会大于0
	month_days := [12]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
	acc_month_days := [13]int{}
	for i := 1; i < 13; i++ {
		acc_month_days[i] += acc_month_days[i-1] + month_days[i-1]
	}
	dayOfWeek := [7]string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
	days += acc_month_days[month-1]
	if month > 2 && ((year%4 == 0 && year%100 != 0) || year%400 == 0) {
		days += 1
	}
	days += day
	return dayOfWeek[days%7]
}

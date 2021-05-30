package main

import "fmt"

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	n := len(s)
	ans := make([]byte, n)
	count := numRows<<1 - 2
	loop := n / count
	lastLoop := n % count
	rows := make([]int, numRows)
	rows[0] = loop
	rows[numRows-1] = loop
	for i := 1; i < numRows-1; i++ {
		rows[i] = loop << 1
	}
	if lastLoop > 0 {
		// rows[0]++
		for i := 0; i < numRows && i < lastLoop; i++ {
			rows[i]++
		}
		if lastLoop > numRows {
			// rows[numRows-1] = loop + 1
			// if lastLoop > numRows {
			for i, row := numRows, numRows-2; i < lastLoop; i++ {
				rows[row]++
				row--
			}
			// }
		}
		loop++
	}
	sumRows := make([]int, numRows+1)
	for i, val := range rows {
		sumRows[i+1] = sumRows[i] + val
	}
	fmt.Println(sumRows)
	for i := 0; i < loop; i++ {
		ans[i] = s[i*count]
		// fmt.Println(i, string(s[i*count]))
		for j := 1; j < numRows-1; j++ {
			if i*count+j >= n {
				return string(ans)
			}
			ans[sumRows[j]+i<<1] = s[i*count+j]
			// fmt.Println(sumRows[j]+i<<1, string(s[i*count+j]))
		}
		if i*count+numRows-1 < n {
			ans[sumRows[numRows-1]+i] = s[i*count+numRows-1]
			// fmt.Println(sumRows[numRows-1]+i, string(s[i*count+numRows-1]))
		}
		for j, row := numRows, numRows-2; j < count; j++ {
			if i*count+j >= n {
				return string(ans)
			}
			ans[sumRows[row]+i<<1+1] = s[i*count+j]
			// fmt.Println(sumRows[row]+i<<1+1, string(s[i*count+j]))
			row--
		}
	}
	return string(ans)
}

func main() {
	s := "PAYPALISHIRING"
	fmt.Println(convert(s, 3))
}

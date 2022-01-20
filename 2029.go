package leetcode

func stoneGameIX(stones []int) bool {
	var one, two, zero int
	for _, v := range stones {
		remainder := v % 3
		if remainder == 0 {
			zero++
		} else if remainder == 1 {
			one++
		} else {
			two++
		}
	}
	// case1: 1 -> 1 -> 2 -> 1 -> 2 -> 1 -> 2 -> ...
	case1 := false
	if one > 0 {
		one-- // Alice先选1
		// Bob选1, Alice选2
		if one > two+1 { // Alice没得选2了，所以输，one恰好比two多1个时是可以选完的
			case1 = false
		}
		if one < two { // Bob没得选1了，所以输即Alice赢
			case1 = true
		}
		if zero&1 == 1 { // 交换先后手
			case1 = !case1
		}
		if one == two || one == two+1 { // 持续到选完都没人输，即Alice输，交换先后手也是Alice输
			case1 = false
		}
		one++
	}
	// fmt.Println(case1)
	if case1 {
		return true
	}
	// case2: 2 -> 2 -> 1 -> 2 -> 1 -> 2
	case2 := false
	if two > 0 {
		two-- // Alice先选2
		// Bob选2, Alice选1
		if one > two { // Bob没得选2了，所以输即Alice赢
			case2 = true
		}
		if one+1 < two { // Alice没得选1了，所以输，two恰好比one多1个时是可以选完的
			case2 = false
		}
		if zero&1 == 1 { // 交换先后手
			case2 = !case2
		}
		if one == two || one+1 == two { // 持续到选完都没人输，即Alice输，交换先后手也是Alice输
			return false
		}
	}
	return case2
}

package leetcode

func validTicTacToe(board []string) bool {
	x_count, o_count := 0, 0
	for _, row := range board {
		for _, c := range row {
			switch c {
			case 'X':
				x_count++
			case 'O':
				o_count++
			}
		}
	}
	if x_count < o_count {
		return false
	} else if x_count == o_count { // 要么都没赢要么玩家2赢即不能玩家1赢
		if check(board, 'X') {
			return false
		} else {
			return true
		}
	} else if x_count == o_count+1 { // 玩家1赢或者都没赢即不能玩家2赢
		if check(board, 'O') {
			return false
		} else {
			return true
		}
	} else { // 玩家1棋子数量最多比玩家2多1个
		return false
	}
	// return false
}

func check(board []string, letter rune) bool {
	for _, row := range board {
		cnt := 0
		for _, c := range row {
			if c != letter {
				break
			} else {
				cnt++
			}
		}
		if cnt == 3 {
			return true
		}
	}
	for i := 0; i < 3; i++ {
		cnt := 0
		for j := 0; j < 3; j++ {
			if board[j][i] == byte(letter) {
				cnt++
			} else {
				break
			}
		}
		if cnt == 3 {
			return true
		}
	}
	cnt1, cnt2 := 0, 0
	for i := 0; i < 3; i++ {
		if board[i][i] == byte(letter) {
			cnt1++
		}
		if board[i][2-i] == byte(letter) {
			cnt2++
		}
	}
	return cnt1 == 3 || cnt2 == 3
}

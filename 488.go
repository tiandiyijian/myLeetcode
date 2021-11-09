package leetcode

import (
	"fmt"
	"sort"
	"strings"
)

func clean(s string) string {
	count := 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			count += 1
		} else {
			if count >= 3 {
				return clean(s[:i-count] + s[i:])
			} else {
				count = 1
			}
		}
	}
	if count < 3 {
		return s
	}
	return s[:len(s)-count]
}

func findMinStep(board string, hand string) int {
	hand_slice := strings.Split(hand, "")
	sort.Strings(hand_slice)
	hand = strings.Join(hand_slice, "")
	q := [][]string{}
	q = append(q, []string{board, hand})
	visit := map[string]bool{}
	key := fmt.Sprintf("%v_%v", board, hand)
	visit[key] = true
	depth := 0
	for len(q) > 0 {
		depth++
		k := len(q)
		for k > 0 {
			k--
			cur_board := q[0][0]
			cur_hand := q[0][1]
			q = q[1:]
			for i := 0; i < len(cur_board)+1; i++ {
				for j := 0; j < len(cur_hand); j++ {
					if j > 0 && cur_hand[j] == cur_hand[j-1] {
						continue
					}
					if i > 0 && cur_board[i-1] == cur_hand[j] {
						continue
					}

					choose := false
					if i > 0 && i < len(cur_board) && cur_board[i-1] == cur_board[i] && cur_board[i] != cur_hand[j] {
						choose = true
					}
					if i < len(cur_board) && cur_board[i] == cur_hand[j] {
						choose = true
					}
					if choose {
						new_board := clean(cur_board[:i] + string(cur_hand[j]) + cur_board[i:])
						if new_board == "" {
							return depth
						}
						new_hand := cur_hand[:j] + cur_hand[j+1:]
						key := fmt.Sprintf("%v_%v", new_board, new_hand)
						if visit[key] {
							continue
						}
						visit[key] = true
						q = append(q, []string{new_board, new_hand})
					}
				}
			}
		}
	}
	return -1
}

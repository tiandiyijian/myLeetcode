package leetcode

func countBattleships(board [][]byte) int {
	m, n := len(board), len(board[0])
	X := byte('X')
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == X && (i == 0 || board[i-1][j] != X) && (j == 0 || board[i][j-1] != X) {
				ans++
			}
		}
	}
	return ans
}

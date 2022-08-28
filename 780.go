package leetcode

func reachingPoints(sx int, sy int, tx int, ty int) bool {
	// 倒推
	for tx >= sx && ty >= sy {
		if sx == tx {
			return (ty-sy)%tx == 0
		}
		if sy == ty {
			return (tx-sx)%ty == 0
		}
		if tx == ty {
			return (sx == 0 && sy == ty) || (sx == tx && sy == 0)
		}
		if tx > ty {
			tx -= ty
		} else {
			ty -= tx
		}
		// fmt.Println(tx, ty)
	}
	return false
}

/*
 * @lc app=leetcode.cn id=304 lang=javascript
 *
 * [304] 二维区域和检索 - 矩阵不可变
 */

// @lc code=start
/**
 * @param {number[][]} matrix
 */
var NumMatrix = function (matrix) {
  let m = matrix.length;
  if (m == 0) return;
  let n = matrix[0].length;
  if (n == 0) return;
  this.dp = Array.from(Array(m + 1), () => Array(n + 1).fill(0));
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      this.dp[i + 1][j + 1] =
        this.dp[i + 1][j] + this.dp[i][j + 1] - this.dp[i][j] + matrix[i][j];
    }
  }
  console.log(this.dp);
};

/**
 * @param {number} row1
 * @param {number} col1
 * @param {number} row2
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function (row1, col1, row2, col2) {
  return (
    this.dp[row2 + 1][col2 + 1] -
    this.dp[row2 + 1][col1] -
    this.dp[row1][col2 + 1] +
    this.dp[row1][col1]
  );
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
// @lc code=end

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5],
];
let a = new NumMatrix(matrix);
console.log(a.sumRegion(2, 1, 4, 3));
console.log(a.sumRegion(1, 1, 2, 2));
console.log(a.sumRegion(1, 2, 2, 4));

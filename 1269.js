/**
 * @param {number} steps
 * @param {number} arrLen
 * @return {number}
 */
var numWays = function (steps, arrLen) {
  const MOD = 1000000007;
  // let col = Math.min(arrLen-1, steps);
  let col = Math.min(arrLen - 1, parseInt(steps / 2));
  // 最多只能走到一半的步数那么远，再远就走不回来了
  const dp = new Array(2).fill(null).map(() => Array(col + 1).fill(0));
  dp[0][0] = 1;
  // console.log(dp);
  for (let i = 1; i <= steps; i++) {
    let row = i & 1;
    for (let j = 0; j <= col; j++) {
      if (i == j) {
        dp[row][j] = 1;
        break;
      }
      if (i < j) break;
      if (j == 0) {
        dp[row][j] = dp[row ^ 1][j] + dp[row ^ 1][j + 1];
      } else if (j == col) {
        dp[row][j] = dp[row ^ 1][j - 1] + dp[row ^ 1][j];
      } else {
        dp[row][j] = dp[row ^ 1][j - 1] + dp[row ^ 1][j] + dp[row ^ 1][j + 1];
      }
      // console.log(dp[i][j])
      dp[row][j] %= MOD;
    }
  }
  return dp[steps & 1][0];
};

/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */
var minKBitFlips = function (A, K) {
  let tmp = 0,
    ans = 0,
    n = A.length;
  for (let i = 0; i < n; i++) {
    if (i >= K && A[i - K] > 1) {
      tmp ^= 1;
      A[i - K] -= 2;  //恢复原数组
    }
    if (A[i] == tmp) {
      if (i + K > n) return -1;
      ans++;
      tmp ^= 1;
      A[i] += 2;  //表示在以这个位置为起点翻转
    }
  }
  return ans;
};

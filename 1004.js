/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */
var longestOnes = function (A, K) {
  let n = A.length,
    l = 0,
    r = 0,
    count = 0,
    ans = 0;
  while (r < n) {
    if (A[r] == 0) count++;
    while (count > K) {
      if (A[l] == 0) count--;
      l++;
    }
    r++;
    ans = Math.max(ans, r - l);
  }
  return ans;
};

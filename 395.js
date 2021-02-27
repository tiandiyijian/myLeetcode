/*
 * @lc app=leetcode.cn id=395 lang=javascript
 *
 * [395] 至少有K个重复字符的最长子串
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function (s, k) {
  let dfs = function (l, r) {
    // console.log(l, r);
    if (l > r) return 0;
    let counter = Array(26).fill(0);
    for (let i = l; i <= r; i++) {
      counter[s.charCodeAt(i) - 97]++;
    }
    let ans = 0;
    let pre = l - 1;
    for (let i = l; i <= r; i++) {
      if (counter[s.charCodeAt(i) - 97] < k) {
        if (i - pre - 1 > ans) {
          let tmp = dfs(pre + 1, i - 1);
          ans = Math.max(ans, tmp);
        }
        pre = i;
      }
    }
    if (pre == l - 1) return r - l + 1;
    let tmp = dfs(pre + 1, r);
    return Math.max(ans, tmp);
  };
  return dfs(0, s.length - 1);
};
// @lc code=end
console.log(longestSubstring('aaabbb', 3));

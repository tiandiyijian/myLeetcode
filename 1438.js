/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var longestSubarray = function (nums, limit) {
  let n = nums.length;
  if (n == 0) return 0;
  let l = 0,
    r = 0,
    ans = 0;
  let max_Q = [],
    min_Q = [];
  while (r < n) {
    while (max_Q && max_Q[max_Q.length - 1] < nums[r]) max_Q.pop();
    while (min_Q && min_Q[min_Q.length - 1] > nums[r]) min_Q.pop();
    max_Q.push(nums[r]);
    min_Q.push(nums[r]);
    while (max_Q[0] - min_Q[0] > limit) {
      if (max_Q[0] == nums[l]) max_Q.shift();
      if (min_Q[0] == nums[l]) min_Q.shift();
      l++;
    }
    r++;
    ans = Math.max(ans, r - l);
  }
  return ans;
};

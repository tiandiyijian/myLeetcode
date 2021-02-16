/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function (nums) {
  nums.sort((a, b) => a - b);
  return nums.reduce((pre, cur, idx) => {
    if (idx % 2 == 0) {
      return pre + cur;
    } else {
      return pre;
    }
  });
};

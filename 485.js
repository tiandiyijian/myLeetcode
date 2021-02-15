/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
  let max_count = (count = 0);
  for (let num of nums) {
    if (num == 1) count++;
    else {
      max_count = max_count > count ? max_count : count;
      count = 0;
    }
  }
  return max_count > count ? max_count : count;
};

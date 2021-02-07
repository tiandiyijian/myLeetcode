/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function (nums) {
  let n = nums.length;

  let r1 = (l1 = 0);
  while (r1 < n - 1 && nums[r1] <= nums[r1 + 1]) r1 += 1;
  // console.log(l1, r1);
  if (r1 == n - 1) return true;

  let r2 = (l2 = r1 + 1);
  while (r2 < n - 1 && nums[r2] <= nums[r2 + 1]) r2 += 1;
  // console.log(l2, r2);

  if (l1 == r1 || l2 == r2) return r2 == n - 1;
  return r2 == n - 1 && (nums[l2] >= nums[r1 - 1] || nums[r1] <= nums[l2 + 1]);
};

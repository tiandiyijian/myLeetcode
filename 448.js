/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function (nums) {
  let n = nums.length;
  for (let i = 0; i < n; i++) {
    ele = nums[i];
    while (nums[ele - 1] != ele) {
      tmp = nums[ele - 1];
      nums[ele - 1] = ele;
      ele = tmp;
    }
  }
  // console.log(nums)
  return nums
    .map((ele, idx) => {
      return ele == idx + 1 ? -1 : idx + 1;
    })
    .filter((ele) => ele > 0);
};

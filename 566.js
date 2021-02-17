/**
 * @param {number[][]} nums
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function (nums, r, c) {
  let m = nums.length,
    n = nums[0].length;
  if (m * n != r * c) return nums;
  let matrix = Array.from(Array(r), () => Array(c).fill(0));
  // console.log(matrix);
  let idx = 0;
  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      matrix[i][j] = nums[parseInt(idx / n)][idx % n];
      idx++;
    }
  }
  return matrix;
};

/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function (A) {
  let m = A.length,
    n = A[0].length;
  let mid = parseInt(n / 2);
  let flag = (n & 1) > 0;
  A.forEach((row) => {
    for (let i = 0; i < mid; i++) {
      if (row[i] == row[n - i - 1]) {
        row[i] ^= 1;
        row[n - i - 1] ^= 1;
      }
    }
    if (flag) row[mid] ^= 1;
  });
  return A;
};

console.log(
  flipAndInvertImage([
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 0],
  ])
);

/**
 * @param {number[]} A
 * @return {boolean}
 */
var isMonotonic = function (A) {
  let n = A.length;
  if (A[0] == A[n - 1])
    return A.every((val, idx) => {
      return idx == n - 1 || val == A[idx + 1];
    });
  else if (A[0] < A[n - 1])
    return A.every((val, idx) => {
      return idx == n - 1 || val <= A[idx + 1];
    });
  else
    return A.every((val, idx) => {
      return idx == n - 1 || val >= A[idx + 1];
    });
};

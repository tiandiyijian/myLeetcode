/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function (arr) {
  let l = 0;
  let n = arr.length;
  let ans = 1;
  let gt = (a, b) => a > b;
  let lt = (a, b) => a < b;
  let compare;
  while (l < n) {
    if (l == n - 1) {
      break;
    }
    if (arr[l] == arr[l + 1]) {
      l += 1;
      continue;
    }
    let r = l;
    if (arr[r] > arr[r + 1]) {
      compare = gt;
    } else if (arr[r] < arr[r + 1]) {
      compare = lt;
    }
    while (r < n - 1 && compare(arr[r], arr[r + 1])) {
      r += 1;
      compare = compare == gt ? lt : gt;
    }
    ans = Math.max(ans, r - l + 1);
    l = r;
  }
  return ans;
};

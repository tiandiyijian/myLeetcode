/**
 * @param {number[]} customers
 * @param {number[]} grumpy
 * @param {number} X
 * @return {number}
 */
var maxSatisfied = function (customers, grumpy, X) {
  let n = customers.length;
  let count = 0;
  for (let i = 0; i < X; i++) {
    if (grumpy[i] == 1) count += customers[i];
  }
  // console.log(count)
  let max_count = count,
    max_count_idx = 0;
  for (let i = 1; i <= n - X; i++) {
    if (grumpy[i - 1] == 1) count -= customers[i - 1];
    if (grumpy[i + X - 1] == 1) count += customers[i + X - 1];
    if (count > max_count) {
      max_count = count;
      max_count_idx = i;
      // console.log(i, count);
    }
  }
  // console.log(max_count, max_count_idx)
  // let ans = 0;
  // for (let i = 0; i < max_count_idx; i++) {
  //     if (grumpy[i] == 0) ans += customers[i];
  // }
  // for (let i = max_count_idx; i < max_count_idx + X; i++) ans += customers[i];
  // for (let i = max_count_idx + X; i < n; i++) {
  //     if (grumpy[i] == 0) ans += customers[i];
  // }
  // return ans
  let total = customers.reduce((pre, cur, idx) => {
    return pre + cur * (1 - grumpy[idx]);
  }, 0);
  // console.log(total, max_count)
  return total + max_count;
};

/**
 * @param {number[]} row
 * @return {number}
 */
var minSwapsCouples = function (row) {
  let n = row.length;
  let pos = Array(n);
  row.forEach((el, idx) => {
    pos[el] = idx;
  });
  let ans = 0;
  for (let i = 0; i < n; i += 2) {
    let mate = row[i] ^ 1;
    if (mate == row[i + 1]) continue;
    let tmp = row[i + 1];
    row[i + 1] = mate;
    row[pos[mate]] = tmp;
    pos[tmp] = pos[mate];
    // pos[mate] = i+1
    ans++;
    // console.log(row)
  }
  return ans;
};

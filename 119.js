/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  if (rowIndex < 2) return Array(rowIndex + 1).fill(1);
  let row = [1, 1];
  for (let k = 2; k <= rowIndex; ++k) {
    let new_row = [1];
    for (let i = 1; i < k; i++) {
      new_row[i] = row[i] + row[i - 1];
    }
    new_row.push(1);
    row = new_row;
  }
  return row;
};

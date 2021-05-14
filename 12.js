/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  let mp = new Map([
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I'],
  ]);
  let ans = '';
  function helper(n) {
    if (num >= n) {
      ans += Array(parseInt(num / n))
        .fill(mp.get(n))
        .join('');
      num %= n;
    }
  }
  for (let k of mp.keys()) {
    helper(k);
  }

  return ans;
};

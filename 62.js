/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
  let total = m + n - 2;
  let a = 1, b = 1;
  iters = Math.min(m, n) - 1;
  for(let i = 0; i < iters; ++i){
      a *= total;
      b *= (i+1);
      total -= 1;
  }
  console.log(a, b);
  return a / b;
};

console.log(uniquePaths(3,2));
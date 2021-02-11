/**
 * @param {number} n
 * @param {number[][]} paths
 * @return {number[]}
 */
var gardenNoAdj = function (n, paths) {
  let neighbor = Array.from(Array(n), () => Array());
  for (const [a, b] of paths) {
    neighbor[a - 1].push(b - 1);
    neighbor[b - 1].push(a - 1);
  }
  let ans = Array(n).fill(0);
  let color = null;
  for (let i = 0; i < n; i++) {
    color = new Set([1, 2, 3, 4]);
    for (const j of neighbor[i]) {
      color.delete(ans[j]);
    }
    ans[i] = Array.from(color)[0];
  }
  return ans;
};

let n = 3;
let paths = [
  [1, 2],
  [2, 3],
  [3, 1],
];
console.log(gardenNoAdj(n, paths));

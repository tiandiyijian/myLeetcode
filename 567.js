/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  let n = s1.length;
  let count = Array(26).fill(0);
  for (let i = 0; i < n; i++) {
    count[s1.charCodeAt(i) - 97]++;
  }
  let window = Array(26).fill(0);
  for (let i = 0; i < n; i++) {
    window[s2.charCodeAt(i) - 97]++;
  }
  if (
    window.every((val, idx) => {
      return val == count[idx];
    })
  )
    return true;
  // console.log(window, count);
  for (let i = n; i < s2.length; i++) {
    window[s2.charCodeAt(i - n) - 97]--;
    window[s2.charCodeAt(i) - 97]++;
    if (
      window.every((val, idx) => {
        return val == count[idx];
      })
    )
      return true;
  }
  return false;
};

let s1 = 'ab';
let s2 = 'ab';
console.log(checkInclusion(s1, s2));

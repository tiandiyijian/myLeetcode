/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */
var subarraysWithKDistinct = function (A, K) {
  const n = A.length;
  function subraraysWithMost(K) {
    let freq = Array(n + 1).fill(0);
    let l = (r = ans = count = 0);
    while (r < n) {
      if (freq[A[r]] == 0) {
        count++;
      }
      freq[A[r]]++;
      r++;
      while (count > K) {
        freq[A[l]]--;
        if (freq[A[l]] == 0) count--;
        l++;
      }
      ans += r - l;
    }
    return ans;
  }
  return subraraysWithMost(K) - subraraysWithMost(K - 1);
};

/**
 * @param {number[]} A
 * @param {number} K
 * @return {number}
 */
var subarraysWithKDistinct2 = function (A, K) {
  const n = A.length;
  const freq1 = new Array(n + 1).fill(0);
  const freq2 = new Array(n + 1).fill(0);
  let l1 = (l2 = r = ans = count1 = count2 = 0);
  while (r < n) {
    if (freq1[A[r]] == 0) {
      count1++;
    }
    if (freq2[A[r]] == 0) {
      count2++;
    }
    freq1[A[r]]++;
    freq2[A[r]]++;
    while (count1 > K) {
      freq1[A[l1]]--;
      if (freq1[A[l1]] == 0) count1--;
      l1++;
    }
    while (count2 > K - 1) {
      freq2[A[l2]]--;
      if (freq2[A[l2]] == 0) count2--;
      l2++;
    }
    ans += l2 - l1;
    r++;
    // console.log(r, l1, l2);
  }
  return ans;
};

console.log(subarraysWithKDistinct2([1, 2, 1, 2, 3], 2));

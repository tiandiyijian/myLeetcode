/*
 * @lc app=leetcode.cn id=1178 lang=javascript
 *
 * [1178] 猜字谜
 */

// @lc code=start
/**
 * @param {string[]} words
 * @param {string[]} puzzles
 * @return {number[]}
 */
var findNumOfValidWords = function (words, puzzles) {
  let word2mask = function (word) {
    let mask = 0;
    for (let i = 0; i < word.length; i++) {
      mask |= (1 << (word.charCodeAt(i) - 97));
    }
    return mask;
  };

  let countOnes = function(num) {
    let count = 0;
    while (num) {
      if (num & 1) count++;
      num >>= 1;
    }
    return count;
  }


  let frequency = new Map();
  for (const i in words) {
    let mask = word2mask(words[i]);
    if (countOnes(mask) <= 7)
      frequency.set(mask, (frequency.get(mask) || 0) + 1);
  }
  // puzzleMask = puzzles.map((puzzle) => word2mask(puzzle));

  let ans = [];

  // for (let i = 0; i < puzzles.length; i++) {
  //   let p_mask = word2mask(puzzles[i]);
  //   let tmp = 0;
  //   frequency.forEach((count, w_mask) => {
  //     if (
  //       (((1 << (puzzles[i].charCodeAt(0) - 97)) & w_mask) > 0) && ((w_mask & p_mask) == w_mask)
  //     )
  //       tmp += count;
  //   })
  //   // words.forEach((w_mask) => {
  //   //   // console.log(w_mask.toString(2), puzzleMask[i].toString(2));
  //   //   // console.log(w_mask & puzzleMask[i], w_mask, (w_mask & puzzleMask[i]) == w_mask, 1==1);
  //   //   // console.log(Boolean(((1 << (puzzles[i].charCodeAt(0) - 97)) & w_mask) > 0));
  //   //   // console.log(Boolean((w_mask & puzzleMask[i]) == w_mask));
  //   //   if (
  //   //     (((1 << (puzzles[i].charCodeAt(0) - 97)) & w_mask) > 0) && ((w_mask & puzzleMask[i]) == w_mask)
  //   //   )
  //   //     count++;
  //   // });
  //   ans[i] = tmp;
  // }
  for (const puzzle of puzzles) {
    let mask = 0, total = 0;
    for (let i = 1; i < 7; ++i) {
        mask |= (1 << (puzzle[i].charCodeAt() - 'a'.charCodeAt()));
    }
    let subset = mask;
    while (subset) {
        let s = subset | (1 << (puzzle[0].charCodeAt() - 'a'.charCodeAt()));
        if (frequency.has(s)) {
            total += frequency.get(s);
        }
        subset = (subset - 1) & mask;
    }
    // 在枚举子集的过程中，要么会漏掉全集 mask，要么会漏掉空集
    // 这里会漏掉空集，因此需要额外判断空集
    if (frequency.has(1 << (puzzle[0].charCodeAt() - 'a'.charCodeAt()))) {
        total += frequency.get(1 << (puzzle[0].charCodeAt() - 'a'.charCodeAt()));
    }
    ans.push(total);
  }
  return ans;
};
// @lc code=end
words =   ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
console.log(findNumOfValidWords(words, puzzles));
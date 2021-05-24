/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function (root, x, y) {
  if (x == y || x == root.val || y == root.val) return false;
  let findX = false,
    findY = false;
  let depthX, depthY;
  let fatherX, fatherY;
  let q = [root];
  let depth = 0;
  function helper(node, father) {
    if (node) {
      q.push(node);
      if (node.val == x) {
        findX = true;
        depthX = depth;
        fatherX = father;
      } else if (node.val == y) {
        findY = true;
        depthY = depth;
        fatherY = father;
      }
    }
  }
  while (q) {
    depth += 1;
    let current_len = q.length;
    for (let i = 0; i < current_len; i++) {
      let node = q.shift();
      helper(node.left, node);
      helper(node.right, node);
    }
    if (findX && findY) {
      return depthX == depthY && fatherX != fatherY;
    }
  }
};

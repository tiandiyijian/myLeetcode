# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 我本来的想法是利用二分查找比当前节点大的第一个元素
    # 官方题解这个直接根据上下界的做法有点妙

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        arr = []
        
        def helper(root: TreeNode):
            if not root:
                return
            arr.append(root.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return ' '.join(list(map(str, arr)))
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split()))
        # print(arr)
        i = 0
        n = len(arr)

        def helper(lower, upper):
            nonlocal i, n
            if i == n or not (lower <= arr[i] <= upper):
                return
            
            val = arr[i]
            i += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        
        return helper(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(node, parent):
            # 其实可以不用传递parent，这种方法是子节点利用父节点的信息确定next，
            # 但其实父节点可以直接确定它的子节点的next,这样就可以很方便的改成递归
            if not node:
                return
            # print(node.val, end=' ')
            if not parent:
                helper(node.left, node)
                helper(node.right, node)
                return
            if node is parent.left:
                node.next = parent.right
            else:
                node.next = parent.next.left if parent.next else None
            # print(node.next.val if node.next else 'None')
            helper(node.left, node)
            helper(node.right, node)

        helper(root, None)
        return root


if __name__ == "__main__":
    s = Solution()
    print()

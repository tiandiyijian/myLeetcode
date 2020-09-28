import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        while q:
            tmp_len = len(q)

            for i in range(tmp_len):
                node = q.popleft()
                # print(tmp_len, node.val)
                if i < tmp_len - 1:
                    node.next = q[0]
                else:
                    node.next = None
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


if __name__ == "__main__":
    s = Solution()
    print()

# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodeToNode = {}
        def DFS(node: 'Node'):
            if not node:
                return None
            if nodeToNode.__contains__(node):
                return nodeToNode[node]
            dup = Node(node.val, [])
            nodeToNode[node] = dup
            for n in node.neighbors:
                clone = DFS(n)
                dup.neighbors.append(clone)
            return dup
        return DFS(node)

    def cloneGraph2(self, node: 'Node') -> 'Node':
        nodeToNode = {}
        done = set()
        queue = [node]
        while queue:
            s = queue.pop(0)
            if done.__contains__(s):
                continue
            done.add(s)
            if nodeToNode.__contains__(s) == False:
                nodeToNode[s] = Node(s.val, [])
            t = nodeToNode[s]
            for n in s.neighbors:
                if nodeToNode.__contains__(n) == False:
                    nodeToNode[n] = Node(n.val, [])
                queue.append(n)
                t.neighbors.append(nodeToNode[n])
        return nodeToNode[node]
    
    def cloneGraph3(self, node: 'Node') -> 'Node':
        if not node:
            return None
        history = {}
        def dfs(node):
            tmp = history.get(node, None)
            if tmp:
                return tmp
            new_node = Node(node.val)
            history[node] = new_node
            for n in node.neighbors:
                tmp_neighbor = dfs(n)
                new_node.neighbors.append(tmp_neighbor)
            return new_node
        return dfs(node)  


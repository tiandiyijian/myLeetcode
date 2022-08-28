from typing import List


class Solution:

    def outerTrees1(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        left, right, top, bottom = [], [], [], []
        # trees.sort(key=lambda x: (x[0], -x[1]))
        for x, y in trees:
            if not left or x == left[0][0]:
                left.append([x, y])
            elif x < left[0][0]:
                left = [[x, y]]

            if not right or x == right[0][0]:
                right.append([x, y])
            elif x > right[0][0]:
                right = [[x, y]]

            if not top or y == top[0][1]:
                top.append([x, y])
            elif y > top[0][1]:
                top = [[x, y]]

            if not bottom or y == bottom[0][1]:
                bottom.append([x, y])
            elif y < bottom[0][1]:
                bottom = [[x, y]]

        if len(left) > 0:
            left.sort()
        if len(right) > 0:
            right.sort()
        if len(top) > 0:
            top.sort()
        if len(bottom) > 0:
            bottom.sort()
        print(left, right, bottom, top)

        ans = list([x, y] for x, y in set((x, y) for x, y in left + right + top + bottom))
        print(ans)
        left_point = left[-1]
        top_point = top[0]
        trees.sort(key=lambda x: (x[0], -x[1]))
        for i, (x, y) in enumerate(trees):
            if x >= top_point[0]:
                break
            if x == left_point[0]:
                continue
            if (y - left_point[1]) / (x - left_point[0]) >= \
                (top_point[1] - left_point[1]) / (top_point[0] - left_point[0]):
                ans.append([x, y])
                left_point = [x, y]
        print(ans)
        
        top_point = top[-1]
        right_point = right[-1]
        for x, y in trees[i:]:
            if x == right_point[0]:
                break
            if x <= top_point[0]:
                continue
            if (top_point[1] - y) / (x - top_point[0]) <= \
                (top_point[1] - right_point[1]) / (right_point[0] - top_point[0]):
                ans.append([x, y])
                top_point = [x, y]
        print(ans)
        
        trees.sort()
        left_point = left[0]
        bottom_point = bottom[0]
        for i, (x, y) in enumerate(trees):
            if x == bottom_point[0]:
                break
            if x == left_point[0]:
                continue
            if (left_point[1] - y) / (x - left_point[0]) >= \
                (left_point[1] - bottom_point[1]) / (bottom_point[0] - left_point[0]):
                ans.append([x, y])
                left_point = [x, y]
        print(ans)
        
        bottom_point = bottom[-1]
        right_point = right[0]
        print(i)
        for x, y in trees[i:]:
            if x == right_point[0]:
                break
            if x <= bottom_point[0]:
                continue
            if (right_point[1] - y) / (right_point[0] - x) >= \
                (right_point[1] - bottom_point[1]) / (right_point[0] - bottom_point[0]):
                ans.append([x, y])
                bottom_point = [x, y]
        print(ans)
        
        return ans

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # CV
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        trees.sort()

        hull = [0]  # hull[0] 需要入栈两次，不标记
        used = [False] * n
        # 求凸包的下半部分
        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        hull.pop()

        return [trees[i] for i in hull]

trees = [[0,0],[1,1],[100,100]]
print(Solution().outerTrees(trees))
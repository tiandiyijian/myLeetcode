"""
class Solution:
    def exist(self, board, word):
        def search(board, word, i, j, currentIndex, dir, res, tag):
            #print('(%d,%d)'% (i,j))
            if board[i][j] != word[currentIndex] or currentIndex >= len(word) or tag[i][j]:
                print('(%d,%d)' % (i, j) + 'false')
                print(tag)
                print(str(currentIndex) + ' ' + str(len(word)))
                return
            if currentIndex == len(word) - 1:
                print('(%d,%d)' % (i, j) + 'true')
                res.append(True)
                return
            if board[i][j] == word[currentIndex]:
                tag[i][j] = True
                if i > 0 and dir != 3:
                    search(board, word, i - 1, j, currentIndex + 1, 1, res, tag)
                if i < len(board) - 1 and dir != 1:
                    search(board, word, i + 1, j, currentIndex + 1, 3, res, tag)
                if j > 0 and dir != 2:
                    search(board, word, i, j - 1, currentIndex + 1, 4, res, tag)
                if j < len(board[0]) - 1 and dir != 4:
                    search(board, word, i, j + 1, currentIndex + 1, 2, res, tag)
                tag[i][j] = False

        width = len(board)
        length = len(board[0])
        if width == length == 1:
            return len(word) == 1 and word == board[0][0]
        for i in range(1):
            for j in range(1):
                tag = [[False] * len(board[0])] * len(board)
                if i > 0:
                    res = [False]
                    search(board, word, i, j, 0, 3, res, tag)
                    if res[-1] == True:
                        return True
                if i < width - 1:
                    res = [False]
                    search(board, word, i, j, 0, 1, res, tag)
                    print(res)
                    if res[-1] == True:
                        return True
                if j > 0:
                    res = [False]
                    search(board, word, i, j, 0, 4, res, tag)
                    if res[-1] == True:
                        return True
                if j < length - 1:
                    res = [False]
                    search(board, word, i, j, 0, 2, res, tag)
                    print(res)
                    if res[-1] == True:
                        return True
        return False

class Solution:
    def recursive(self, can, board, word, pre):
        if len(pre) == len(word):
            return True
        for i in can:
            if (0 <= i[0] < self.shape[0]) and (0 <= i[1] < self.shape[1]) and word[len(pre)] == board[i[0]][i[1]] and i not in pre:
                pre[i] = 1
                if self.recursive([(i[0]-1, i[1]), (i[0]+1, i[1]), (i[0], i[1]-1), (i[0], i[1]+1)], board, word, pre):
                    return True
                del pre[i]
        return False

    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        self.shape = (len(board), len(board[0]))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if board[i][j] == word[0]:
                    pre = {}
                    if self.recursive([(i, j)], board, word, pre):
                        return True
        return False
"""
class Solution:
    def exist(self, board, word):
        def legal(index, board):
            return 0 <= index[0] < len(board) and 0 <= index[1] < len(board[0])
        def findWord(currentIndexs, board, word, indexs):
            if len(word) == len(indexs):
                return True
            for index in currentIndexs:
                if legal(index, board) and word[len(indexs)] == board[index[0]][index[1]] and index not in indexs:
                    indexs.append(index)
                    if findWord([(index[0] - 1, index[1]), (index[0] + 1, index[1]), (index[0], index[1] - 1), (index[0], index[1] + 1)], board, word, indexs):
                        return True
                    indexs.pop()
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    indexs = []
                    if findWord([(i,j)], board, word, indexs):
                        return True
        return False
    
    def exist2(self, board, word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            # 这一行很关键，起初我担心如果记录访问过的节点可能会导致错过答案
            # 但是要意识到记录访问过的节点的目的是怕图中存在环
            # 所以递归回溯到一个节点的时候完全可以把这个节点从记录中删除掉
            # 这样也就不会错过答案
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False
    

if __name__ == '__main__':
    board = [["a","a","a","a"], ["a","a","a","a"],["a","a","a","a"]]
    word = "aaaaaaaaaaaaaaaaaaaa"
    a = Solution()
    print(a.exist(board, word))
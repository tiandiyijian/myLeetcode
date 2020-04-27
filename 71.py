class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        def pathToList(path, dirs):
            length = len(path)
            tem = ''
            flag = 0
            for i in range(length):
                if path[i] == '/':
                    while i + 1 < length and path[i+1] == '/':
                        i+=1
                    if tem != '':
                        if tem != '.':
                            if tem == '..' and len(dirs) > 0:
                                dirs.pop()
                            if tem != '..':
                                dirs.append(tem)
                        tem = ''
                else:
                    tem += path[i]
            if tem != '':
                if tem != '.':
                    if tem == '..' and len(dirs) > 0:
                        dirs.pop()
                    if tem != '..':
                        dirs.append(tem)
        dirs = []
        pathToList(path, dirs)
        print(dirs)
        return '/' + '/'.join(dirs)

if __name__ == '__main__':
    path = '/a//b////c/d//././/..'
    print(path.split('/'))

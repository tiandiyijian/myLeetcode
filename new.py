import sys
import os

if __name__ == "__main__":
    # print(os.getcwd())
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if '.' not in name:
            name += '.py'
        contain_list = True if len(sys.argv) > 1 and sys.argv[-1] == 'l' else False
        if os.path.exists(name):
            print("File exists!")
        else:
            f = open(name, 'w')
            if contain_list:
                f.write('from typing import List\n')
            for i in range(4):
                f.write('\n')
            f.write('if __name__ == "__main__":\n')
            f.write('    s = Solution()\n')
            f.write('    print()')
            f.close()
            

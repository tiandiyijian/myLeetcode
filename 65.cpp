#include <iostream>
#include <string>

using namespace std;

class Solution {
private:
    bool scanInteger(string &s, int &i) {
        if (s[i] == '+' || s[i] == '-')
            ++i;
        return scanUnsignedInteger(s, i);
    }

    bool scanUnsignedInteger(string &s, int &i) {
        int before = i;
        while (i < s.size() && s[i] <= '9' && s[i] >= '0') ++i;
        return i > before;
    }

public:
    bool isNumber(string s) {
        if (s.empty()) return 0;
        
        int i = 0, len = s.size();
        
        while (s[i] == ' ') ++i; //跳过开头空格
        
        bool isNum = scanInteger(s, i); 
        // cout << "1: i: " << i << " isNum: " << isNum << endl;       
        
        if (s[i] == '.') {
            ++i;
            isNum = scanUnsignedInteger(s, i) || isNum; //小数点前面后面都可以没有数字，但不能都没有
            // cout << "2: i: " << i << " isNum: " << isNum << endl; 
        }
        
        if (s[i] == 'e' || s[i] == 'E') {
            ++i;
            isNum = scanInteger(s, i) && isNum; //e前面后面都要有数字
            // cout << "3: i: " << i << " isNum: " << isNum << endl; 
        }

        while (s[i] == ' ') ++i; //跳过结尾空格
        
        // cout << "4: i: " << i << " isNum: " << isNum << endl; 
        return isNum && i == len;
    }
};

int main(int argc, char const *argv[])
{
    auto s = Solution();
    cout << s.isNumber("1.33e-67");
    return 0;
}

#include <iostream>

using namespace std;

class Solution {
private:
    bool matchCore(string &s, int i, string &p, int j) {
        if (j == p.size()) {
            if (i == s.size()) return true;
            return false;
        }

        if (p[j + 1] == '*') {
            if (s[i] == p[j] || (p[j] == '.' && i < s.size())) {
                return matchCore(s, i + 1, p, j) //保留在当前状态
                || matchCore(s, i + 1, p, j + 2) //进入状态机下一个状态
                || matchCore(s, i, p, j + 2);    //忽略a*
            }
            else return matchCore(s, i, p, j + 2);
        }

        // cout << s[i] << " " << p[j] << endl;
        if (s[i] == p[j] || (p[j] == '.' && i < s.size())) {
               //cout << i << " " << j << endl;
                return matchCore(s, i + 1, p, j + 1);
        }

        return false;
    }

public:
    bool isMatch(string s, string p) {
        // if (s.empty() || p.empty()) return false;
        // return matchCore(s, 0, p, 0);
        int lens = s.size(), lenp = p.size();
        bool dp[lens + 1][lenp + 1];
        
        for(int i = 0; i <= lens; ++i)
            for(int j = 0; j <= lenp; ++j)
                dp[i][j] = false;
        
        dp[0][0] = true;
        for(int i = 1; i <= lenp; ++i) {
            if (p[i-1] == '*') dp[0][i] = dp[0][i-2]; //像a*b*这种其实和空串是匹配的
        }
        
        for(int i = 1; i <= lens; ++i) {
            for(int j = 1; j <= lenp; ++j) {
                if (s[i-1] == p[j-1] || p[j-1] == '.') dp[i][j] = dp[i-1][j-1];       
                else if (p[j-1] == '*')
                {
                    dp[i][j] = dp[i][j-2]; //a*可以不算数
                    if (p[j-2] == s[i-1] || p[j-2] == '.')
                    {
                        dp[i][j] = dp[i][j] || dp[i-1][j]; //a*算数而且可以算多次,比如说xaa和xa*
                        /*
                                p   x   a   *    
                            S   T   F   F   F          
                            x   F   T   F   T dp[1][3] = dp[1][3-2]     
                            a   F   F   T   T dp[2][3] = dp[1][3]
                            a   F   F   F   T dp[3][3] = dp[2][3]
                        */
                    }
                }
                else dp[i][j] = false;
            }
        }
        return dp[lens][lenp];
    }
};

int main(int argc, char const *argv[])
{
    string s("123"), p("123*");
    Solution so = Solution();
    cout << so.isMatch(s, p);
    return 0;
}

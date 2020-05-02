#include <iostream>
#include <string>

using namespace std;

// static const auto _____ = []() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
//     return nullptr;
// }();

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s == "") return 0;
        int res = 0, j = 0;
        int index[256] = {0};
        for(int i = 0; j < s.size(); j++)
        {
            i = max(i, index[s[j]]);
            res = max(res, j - i + 1);
            index[s[j]] = j + 1;
        }
        return res;
    }
};

int main() {
    Solution s = Solution();
    string a = "abcdabc";
    std::cout << s.lengthOfLongestSubstring(a);
}
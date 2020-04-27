#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> emptySet;
        vector<vector<int>> res;
        res.push_back(emptySet);
        for (auto num : nums)
        {
            int len = res.size();
            for(int i = 0; i < len; ++i) {
                vector<int> tem(res[i]);
                tem.push_back(num);
                cout << tem.size();
                res.push_back(tem);
            }
        }
        return res;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> e({1, 2, 3});
    Solution s = Solution();
    auto res = s.subsets(e);
    for (auto set : res)
    {
        for(auto i: set) cout << i << " ";
        cout << endl;
    }
    // for (auto &&i : e)
    // {
    //     i *= i;
    // }
    

    // for (auto &i : e)
    // {
    //     cout << i << " ";
    // }

    // int a = 233;
    // int *b = &a;
    // int &c = a;
    // int d = a;
    // cout << a << " " << *b << " " << c << " " << d << endl;
    // a = 2;
    // cout << a << " " << *b << " " << c << " " << d << endl;
    // return 0;
}

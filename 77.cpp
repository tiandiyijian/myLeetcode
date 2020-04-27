#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        if (n < 1 || n < k || k < 1) return {};
        helper(1, k, n);
        return ans;
    }

private:
    vector<int>set;
    vector<vector<int>> ans;

    void helper(int start, int k, int n) {
        if (set.size() == k) {
            ans.push_back(set);
            return;
        }
        for (int i = start; i <= n + 1 - (k - set.size()); i++)
        {
            set.push_back(i);
            helper(i+1, k, n);
            set.pop_back();
        }
        
    }
};
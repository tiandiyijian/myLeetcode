#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 2) return nums.size();
        int subscript = 1;
        for (int i = 1; i < nums.size(); ++i) {
            if (nums[i] != nums[i-1]) nums[subscript++] = nums[i];
        }
        return subscript;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> a = {1,2,2,3,3,4,4};
    cout << s.removeDuplicates(a) << endl;
    return 0;
}

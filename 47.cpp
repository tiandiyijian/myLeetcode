#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        //sort(nums.begin(), nums.end());
        search(res, nums, 0);
        return res;
    }

    void search(vector<vector<int>> &res, vector<int> &nums, int pos) {
        if (pos == nums.size()) {
            // for(vector<int> t : res) {
            //     if(t == nums) return;
            // }
            res.push_back(nums);
            cout << "pos:" << pos << endl;
        }else {
            for(int i = pos; i < nums.size(); ++i) {
                int ifContinue = 0;
                for(int j = i + 1; j < nums.size(); ++j) {
                    if(nums[j] == nums[i]) ifContinue = 1;
                }
                if(ifContinue) continue;
                swap(nums, i, pos);
                //cout << "i:" << i << " pos:" << pos << endl;
                search(res, nums, pos + 1);
                swap(nums, i, pos);
                //while(nums[i+1] == nums[i]) ++i;
            }
        }
    }

    void swap(vector<int> &nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
};
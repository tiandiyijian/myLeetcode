class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> nums;
        for(int i = 0; i < n; ++i) nums.push_back(i+1);
        int tar = k - 1;
        string res;
        //int groupNumber, number, lastGroupNumber = -1;
        while(1) {
            if(tar > 0) {
                int div = fac(--n);
                int num = tar / div;
                tar = tar % div;
                res += to_string(nums[num]);
                nums.erase(nums.begin() + num);
            }else if(tar == 0) {
                for(auto i : nums) res += to_string(i);
                break;
            }
        }
        return res;
    }

    int fac(int n) {
        int res = n;
        while(--n) {
            res *= n;
        }
        return res;
    }
};

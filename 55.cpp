class Solution {
public:
    bool canJump(vector<int>& nums) {
        int zeroCount = 0;
        for(int i = nums.size() - 2; i >= 0; --i) {
            if(nums[i] <= zeroCount) ++zeroCount;
            else zeroCount = 0;
        }
        return zeroCount == 0;
    }
};
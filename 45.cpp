class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.size() == 1) return 0;
        int res = 0, min = 0, max = 0;
        while(1) {
        	findMaxIndex(min, max, nums);
        	++res;
        	if(max >= nums.size() - 1) return res;
        }
    }
    
    void findMaxIndex(int &min, int &max, const vector<int>& nums) {
        int tmax = max, tmin = min;
        int i = min;
        //while()
        for(; i <= tmax; ++i) {
        	if(nums[i] + i > max) {
                max = nums[i] + i; 
                tmin = i;
            }       	
        }
        min = tmin + 1;
    }
};
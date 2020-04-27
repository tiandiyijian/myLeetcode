#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
  		if(nums.size() == 1) return nums[0];
  		int res = nums[0];
  		int tem = res;
  		for(int i = 1; i < nums.size(); ++i) {
  			if(tem <= 0 && nums[i] <= 0) {
  				tem = nums[i];
  			}
  			else if(tem > 0 && nums[i] <= 0) {
  				tem += nums[i];
  			}
  			else if(tem <= 0 && nums[i] >= 0) {
  				tem = nums[i];
  			}
  			else if(tem > 0 && nums[i] > 0) {
  				tem += nums[i];
			}
			if(tem > res) res = tem;
  		}
  		return res;
    }
};

int maxSubArray(vector<int>& nums) {
	int max = nums[0];
	int temSum = 0;
	for (int i = 0; i < nums.size(); ++i)
	{
		temSum += nums[i];
		if(temSum > max) max = temSum;
		if(temSum < 0) temSum = 0;
	}
	return max;
}
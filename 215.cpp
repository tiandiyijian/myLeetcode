#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int lo =  0, hi =  nums.size()-1;
        while (1)
        {
            int mid = paration(nums, lo, hi);
            if (mid == k-1) return nums[mid];
            else if (mid > k-1) {
                hi = mid - 1;
            }
            else lo = mid + 1;
        }
        return nums[k-1];
    }

    int paration(vector<int>& nums, int lo, int hi) {
        int pivot = nums[lo];
        while (lo < hi) {
            while (lo < hi && pivot >= nums[hi]) {
                --hi;
            }
            nums[lo] = nums[hi];
            while (lo < hi && pivot <= nums[lo]) {
                ++lo;
            }
            nums[hi] = nums[lo];
        }
        nums[lo] = pivot;
        return lo;
    }
};
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size(), n = nums2.size();
		if(m > n){
			return findMedianSortedArrays(nums2, nums1);
		}
		int iMin = 0, iMax = m, halfLen = (m + n + 1)/2;
		while(iMin <= iMax){
			int i = (iMax + iMin)/2;
			int j = halfLen - i;
			if(i < iMax && nums1[i] < nums2[j-1]){
				iMin = i + 1;
			}
			else if(i > iMin && nums1[i-1] > nums2[j]){
				iMax = i - 1;
			}
			else{
				int maxLeft = 0;
				if(i == 0) maxLeft = nums2[j-1];
				else if(j == 0) maxLeft = nums1[i-1];
				else maxLeft = nums2[j-1] - nums1[i-1] > 0 ? nums2[j-1] : nums1[i-1];
				if((m + n) % 2 != 0) return maxLeft;

				int minRight = 0;
				if(i == m) minRight = nums2[j];
				else if(j == n) minRight = nums1[i];
				else minRight = nums2[j] - nums1[i] > 0 ? nums1[i] : nums2[j];
				return (maxLeft + minRight)/2.0;
			}
		}
		return 0.0;
    }
};
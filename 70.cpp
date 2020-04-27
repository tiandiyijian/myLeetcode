class Solution {
public:
    int climbStairs(int n) {
  		int[n + 1] res;
        res[1] = 1;
        res[2] = 2;
        for(int i = 3; i <= n; ++i) res[n] = res[n-1] + res[n-2];
        return res[n]; 
    }
};
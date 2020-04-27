#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int maxProfit = 0;
        int i = 0;        
        while (i < prices.size() - 1) {
            while (i < prices.size() - 1 && prices[i] >= prices[i+1]) { // 找到一个递减区间内的最小值
                ++i;
            }
            int low = prices[i];
            while (i < prices.size() - 1 && prices[i] <= prices[i+1]) { // 找到该递增区间的最大值
                ++i;
            }
            maxProfit += (prices[i] - low);
        }
        return maxProfit;
    }

    int maxProfit1(vector<int>& prices) {
        if (prices.empty()) return 0;
        int maxProfit = 0;
        for (int i = 1; i < prices.size(); i++)
        {
            if (prices[i] > prices[i-1]) maxProfit += prices[i] - prices[i-1];
        }
        return maxProfit;
    }
};
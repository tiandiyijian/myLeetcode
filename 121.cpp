#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int len = prices.size();
        vector<int> profit(len, 0);
        int i = 0;
        while (i < len)
        {
            while (i < len - 1 && prices[i] >= prices[i+1])
            {
                ++i;
            }
            int low = prices[i]; //找到一个局部最小值并记录
            while (i < len && prices[i] >= low) //寻找最大利益直到出现比这个局部最小值更小的值即新的局部最小值
            {
                if (prices[i] - low > maxProfit) {
                    maxProfit = prices[i] - low; //更新最大利益
                }
                ++i;
            }
            
        }
        return maxProfit;
    }
};

int main(int argc, char const *argv[])
{
    vector<int> a({7,1,5,3,6,4});
    Solution s = Solution();
    cout << s.maxProfit(a);
    return 0;
}

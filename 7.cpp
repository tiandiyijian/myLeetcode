#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        int pop = 0;
        while (x != 0) {
            pop = x % 10;
            if (ans > INT_MAX/10 || (ans == INT_MAX / 10 && pop > 7)) return 0;
            if (ans < INT_MIN/10 || (ans == INT_MIN / 10 && pop < -8)) return 0;
            ans = ans * 10 + pop;
            x /= 10;
        }
        return ans;
    }
};

int main(int argc, char const *argv[])
{
    cout << -21 % 10;
    return 0;
}

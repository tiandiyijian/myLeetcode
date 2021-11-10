import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countPairs(int[] deliciousness) {
        final int MOD = 1000000007;
        int maxVal = 0;
        for (int val : deliciousness) {
            maxVal = Math.max(val, maxVal);
        }
        int maxSum = maxVal << 1;
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int n = deliciousness.length;
        for (int i = 0; i < n; i++) {
            int val = deliciousness[i];
            for (int sum = 1; sum <= maxSum; sum <<= 1) {
                if (sum < val) {
                    continue;
                }
                int count = map.getOrDefault(sum - val, 0);
                ans = (ans + count) % MOD;
            }
            map.put(val, map.getOrDefault(val, 0) + 1);
        }
        return ans;
    }
}
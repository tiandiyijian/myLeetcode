import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxProduct(String[] words) {
        Map<Integer, Integer> mp = new HashMap<Integer, Integer>();
        int length = words.length;
        for (int i = 0; i < length; i++) {
            int mask = 0;
            int wordLength = words[i].length();
            for (int j = 0; j < wordLength; j++) {
                mask |= 1 << (words[i].charAt(j) - 'a');
            }
            if (wordLength > mp.getOrDefault(mask, 0)) {
                mp.put(mask, wordLength);
            }
        }
        int ans = 0;
        for (int mask1 : mp.keySet()) {
            int len1 = mp.get(mask1);
            for (int mask2 : mp.keySet()) {
                if ((mask1 & mask2) == 0) {
                    int len2 = mp.get(mask2);
                    if (len1 * len2 > ans) {
                        ans = len1 * len2;
                    }
                }
            }
        }
        return ans;
    }
}
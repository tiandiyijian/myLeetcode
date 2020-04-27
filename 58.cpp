#include <cctype>
class Solution {
public:
    int lengthOfLastWord(string s) {
    	int res = 0, flag = 0;
  		for(int i = s.size() - 1; i >= 0; --i) {
  			if(isalpha(s[i])) {
  				++res;
  				flag = 1;
  			}
  			if(s[i] == ' ' && flag == 0) continue;
  			if(s[i] == ' ' && flag == 1) break;
  		}
  		return res;
    }
};
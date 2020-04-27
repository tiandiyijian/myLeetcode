#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if(s.empty()) return s;
        string res;
        for (int i = 0; i < s.length(); ++i)
        {
        	string s1, s2;
        	s1 = expandString(s, i, i);
        	s2 = expandString(s, i, i+1);
        	s1 = s1.length() > s2.length() ? s1 : s2;
        	res = s1.length() > res.length() ? s1 : res; 
        }
        return res;
    }

    string expandString(const string &s, int l, int r) {
    	while(l >= 0 && r < s.length() && s[l] == s[r]) {
    		--l;
    		++r;
    	}
    	return s.substr(l + 1, r - l - 1);
    }
};
class Solution {
public:
    string addBinary(string a, string b) {
        int la = a.length();
        int lb = b.length();
        string res;
        int u = 0, d = 0；
    	int jinwei = 0;
    	int i = lb - 1, j = la - 1;
    	for(; i >= 0 && j >= 0; --i) {
				u = a[i] - '0';
				d = b[j] - '0';      	
    		jinwei = (u&d)|(u^jinwei)|(d^jinwei);
    		sum = u ^ d ^ jinwei;
    		res.push_front(sum + '0');
    		--j;
    	}
    	if(la > lb) {
    		for(int p = i; p >= 0; --p) res.push_front(a[p]);
    	}else {
    		for(int p = j; p >= 0; --p) res.push_front(b[p]);
    	}
    	return res;
    }
};

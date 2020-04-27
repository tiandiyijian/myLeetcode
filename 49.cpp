class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
    	if(strs == NULL) return NULL;
    	hash_map<string, vector<string>> m;
    	for(auto s : strs) {
    		string t = s;
    		sort(s.begin(), s.end());
    		m[s].push_back(t);
    	}
    	vector<vector<string>> res;
    	auto it = m.begin();
    	while(it != m.end()) {
    		res.push_back(it -> second);
    		++it;
    	}
    	return res;
    }
};  
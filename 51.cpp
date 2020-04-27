class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
  		stack<vector<int>> s;
  		vector<vector<int>> res;
        vector<int> empty;
  		s.push(empty);
  		while(!s.empty()) {
  			auto top = s.top();
  			s.pop();
  			if(top.size() == n) {
  				res.push_back(top);
  			}else {
  				for(int i = 0; i < n; ++i) {
  					if(valid(i, top)) {
  						top.push_back(i);
                        s.push(top);
                        for(int i : top) cout << i << " ";
                        cout << endl;
                    	top.pop_back();
  					}
  				}
  			}
  		}
  		vector<vector<string>> solve;
  		string str;
  		for(int i = 0; i < n; ++i) str += ".";
  		for(auto v : res) {
  			vector<string> midium;
  			for(int i = 0; i < n; ++i) {
 				string tem = str;
 				str[v[i]] = 'Q';
 				midium.push_back(str);
  			}
  			solve.push_back(midium);
  		}
  		return solve;
    }

    bool valid(int col, const vector<int> &res) {
    	for(int j = 0; j < res.size(); ++j) {
    		if(ab(res[j] - col) == ab(j - res.size()) || col == res[j]) {
    			cout << j << " " << res[j] << endl << res.size() << " " << col << endl;
    			return false;
    		}
    	}
    	//cout << "start judge\n";
        //for(int i : res) cout << i << " " << res[i] << endl;
        //cout << "judge " << res.size() << " " << col << "end" << endl; 
    	//if(!res.empty()) cout << ab(res[0] - col) << " " <<  ab(0 - res.size()) << endl;
        return true;
    }

    int ab(int r) {
    	return r >= 0 ? r : (-r);
    }
};
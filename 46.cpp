class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
  		vector<vector<int>> res;
  		search(res, nums, 0);
  		return res;
    }

    void search(vector<vector<int>> &res, vector<int> &nums, int pos) {
    	if (pos == nums.size()) {
    		res.push_back(nums);
            cout << "pos:" << pos << endl;
    	}else {
    		for(int i = pos; i < nums.size(); ++i) {
    			swap(nums, i, pos);
                cout << "i:" << i << " pos:" << pos << endl;
                search(res, nums, pos + 1);
    			swap(nums, i, pos);
    		}
    	}
    }

    void swap(vector<int> &nums, int i, int j) {
    	int t = nums[i];
    	nums[i] = nums[j];
    	nums[j] = t;
    }
};
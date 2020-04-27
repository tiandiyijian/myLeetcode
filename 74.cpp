int OneB(const vector<vector<int>>& matrix, int index) {
	return matrix[index / matrix[0].size()][index % matrix[0].size()];
}

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
    	int l = 0, r = matrix.size() * matrix[0].size();
    	while(l <= r) {
    		int mid = (l + r) / 2;
    		if(OneB(matrix, mid) == target) return true;
    		else if(OneB(matrix, mid) > target) r = mid - 1;
    		else l = mid + 1;
    	}
    	return false;
    }
};


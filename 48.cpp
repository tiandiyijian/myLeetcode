class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        vector<vector<int>> m = matrix;
        for(int i = 0; i < matrix.size(); ++i) {
        	for(int j = 0; j < matrix.size(); ++j) {
        		matrix[i][j] = m[matrix.size() - j - 1][i];
        	}
        }
    }
};
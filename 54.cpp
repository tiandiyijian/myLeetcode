#include <vector>

using namespace std;

class Solution {
public:
	int currentRow = 0;
	int currentCol = 0;
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int cols = matrix[0].size();
        int rows = matrix.size();
        vector<int> res;
        int dir = 0, count = cols;
        while(count > 0) {
        	addToRes(res, count, dir, matrix);
        	if(dir == 0 || dir == 2) {
        		rows -=1;
        		count = rows;
        	}else {
        		cols -= 1;
        		count = cols;
        	}
        	dir = (dir+1) % 4;
        }
        return res;
    }

    void addToRes(vector<int> &res, const int &count,
    	const int &dir, const vector<vector<int>>& matrix) {
    	int row = currentRow;
    	int col = currentCol;
    	if(dir == 0) {
    		while(col < currentCol + count) {
    			res.push_back(matrix[row][col]);
    			col += 1;
    		}
    		currentRow += 1;
    		currentCol = col - 1;
    	}else if(dir == 1) {
    		while(row < currentRow + count) {
    			res.push_back(matrix[row][col]);
    			row += 1;
    		}
    		currentRow = row - 1;
    		currentCol -= 1;
    	}else if(dir == 2) {
    		while(col > currentCol - count) {
    			res.push_back(matrix[row][col]);
    			col -= 1;
    		}
    		currentRow -= 1;
    		currentCol = col + 1;
    	}else {
    		while(row > currentRow - count) {
    			res.push_back(matrix[row][col]);
    			row -= 1;
    		}
    		currentRow = row + 1;
    		currentCol += 1;
    	}
    }
};
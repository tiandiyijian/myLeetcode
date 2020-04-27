/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
int x = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  return 0;
}();

class Solution {
public:
    vector<int> postorder(Node* root) {
     	vector<int> res;
     	if (!root)
     	{
     		return res;
     	}
     	stack<Node*> s;
        s.push(root);
     	Node* tem = root;
     	while(!s.empty()) {
     		if (!is_a_father_of_b(s.top(), tem))
     		{
     			go(s);
     		}
     		tem = s.top();
     		s.pop();
     		res.push_back(tem->val);
     	}
     	return res;
    }

    void go(stack<Node*> &s) {
    	while (1){
    		Node* tem = s.top();
    		if (!tem) break;
    		else {
    			auto c = tem->children;
    			if(!c.empty()) {
    				for (int i = c.size() - 1; i >= 0; --i){
    					s.push(c[i]);
    				}
    			}
    			else{
    				break;
    			}
    		}
    	}
	}

    bool is_a_father_of_b(Node* a, Node* b) {
    	for(Node* t : a->children) {
    		if (t == b) return true;
    	}
    	return false;
    }
};
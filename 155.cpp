#include <vector>
#include <stack>
#include <utility>
#include <iostream>

using namespace std;

class MinStack {

private:
    stack<int> min;
    stack<pair<int, int> > s;
    // int min;

public:
    /** initialize your data structure here. */
    MinStack() {
        // min = 0x80000000;
    }
    
    void push(int x) {
        if (s.empty() || getMin() > x) {
            s.push(make_pair(x, x));
        }else {
            s.push(make_pair(x, getMin()));
        }
    }
    
    void pop() {
        if (!s.empty()) s.pop();
    }
    
    int top() {
        return s.top().first;
    }
    
    int getMin() {
        return s.top().second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

int main(int argc, char const *argv[])
{
    MinStack a;
    a.push(1);
    a.push(2);
    cout << a.getMin();
    return 0;
}

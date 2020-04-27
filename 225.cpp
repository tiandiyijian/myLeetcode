#include <queue>

using namespace std;

class MyStack {
private:
    queue<int> q1, q2;

public:
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        if (q2.empty())
        {
            q1.push(x);
        }else 
            q2.push(x);
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int top = 0;
        if (q2.empty())
        {
            int n = q1.size();
            while (--n)
            {
                q2.push(q1.front());
                q1.pop();
            }
            top = q1.back();
            q1.pop();
        }else {
            int n = q2.size();
            while (--n)
            {
                q1.push(q2.front());
                q2.pop();
            }
            top = q2.back();
            q2.pop();
        }
        return top;
    }
    
    /** Get the top element. */
    int top() {
        return q1.empty() ? q2.back() : q1.back();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
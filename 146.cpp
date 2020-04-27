#include <iostream>

using namespace std;

class LRUCache {
private:
    int *_key, *_value, *_time;
    int pointer, _capacity, currentTime;
public:
    LRUCache(int capacity) {
        _key = new int[capacity];
        _value = new int[capacity];
        _time = new int[capacity];
        pointer = 0;
        _capacity = capacity;
        currentTime = 0;
    }
    
    int get(int key) {
        // bool contain = false;
        for (int i = 0; i < pointer; ++i)
        {
            if (_key[i] == key) {
                _time[i] = currentTime++;
                return _value[i];
            }
        }
        return -1;
    }
    
    void put(int key, int value) {
        bool contain = false;
        for (int i = 0; i < pointer; ++i)
        {
            if (_key[i] == key) {
                _key[i] = key;
                _value[i] = value;
                _time[i] = currentTime++;
                contain = true;
                // break;
                return;
            }
        }
        if (!contain) {
            if (pointer < _capacity) {
                _key[pointer] = key;
                _value[pointer] = value;
                _time[pointer] = currentTime++;
                ++ pointer;
            } else {
                int subscript = 0;
                for (int i = 0; i < pointer; i++)
                {
                    if (_time[subscript] > _time[i]) subscript = i;
                }
                _key[subscript] = key;
                _value[subscript] = value;
                _time[subscript] = currentTime++;
            }
        }
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

int main(int argc, char const *argv[])
{
    LRUCache cache = LRUCache(2);

    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cout << cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cout << cache.get(1);       // returns -1 (not found)
    cout << cache.get(3);       // returns 3
    cout << cache.get(4);       // returns 4
}

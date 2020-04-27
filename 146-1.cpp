#include <iostream>
#include <unordered_map>
#include <list>

using namespace std;

class LRUCache {
private:
    unordered_map<int, list<pair<int, int> >::iterator> dict;
    list<pair<int, int> > cache;
    int _capacity;

public:
    LRUCache(int capacity) {
        _capacity = capacity;
    }
    
    int get(int key) {
        const auto it = dict.find(key);
        if (it == dict.cend()) return -1;
        cache.splice(cache.begin(), cache, it->second);
        // cout << (it->second == cache.begin() ? "t" : "f") << endl;
        return it->second->second;
    }
    
    void put(int key, int value) {
        const auto it = dict.find(key);
        if (it != dict.cend()) {
            it->second->second = value;
            cache.splice(cache.begin(), cache, it->second);
            return;
        }
        //key不存在
        //已达到容量
        if (cache.size() == _capacity) {
            const auto& last = cache.back();
            dict.erase(last.first);
            cache.pop_back();
        }
        //添加到头部
        cache.emplace_front(key, value);
        // cache.push_front(make_pair(key, value));
        dict[key] = cache.begin();
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

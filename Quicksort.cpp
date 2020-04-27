#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &nums, int lo, int hi) { //区间为[lo, hi]
        swap(nums[lo], nums[lo + rand()%(hi - lo + 1)]); //随机选取一个元素与首元素交换
        int pivot = nums[lo];
        while (lo < hi) {
            while (lo < hi && pivot <= nums[hi]) {
                --hi;
            }
            nums[lo] = nums[hi];
            while (lo < hi && pivot >= nums[lo]) {
                ++lo;
            }
            nums[hi] = nums[lo];
        }
        nums[lo] = pivot;
        return lo;    
}

void quickSort(vector<int> &nums, int lo, int hi) { //0 <= lo < hi <= size， 区间为[lo, hi)
    if (hi - lo < 2) return; //只有一个元素
    int mi = partition(nums, lo, hi - 1);
    quickSort(nums, lo, mi);
    quickSort(nums, mi + 1, hi);
}

int main(int argc, char const *argv[])
{
    vector<int> a({1, 3, 2, 4});
    quickSort(a, 0, 4);
    for (auto i : a)
    {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}

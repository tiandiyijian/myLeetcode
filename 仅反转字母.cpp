#include <iostream>
#include <vector>
#include <typeinfo>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    char a = 's';
    auto b = 2;
    auto s = "ab";
    cout << s[0] << typeid(s[0]).name() << endl;
    return 0;
}

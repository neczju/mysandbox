#include <iostream>

using namespace std;

int main()
{
    using alias1 = int;
    alias1 zmienna{0};
    cout << "zmienna = " << zmienna << endl;
    typedef int alias2;
    alias2 zmienna2{2};
    cout << "zmienna2 = " << zmienna2 << endl;
}

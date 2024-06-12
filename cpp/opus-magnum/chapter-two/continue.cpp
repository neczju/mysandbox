#include <iostream>

using namespace std;

int main()
{
    for(int k = 0; k < 12; k = k + 1)
    {
        cout << "A";
        if(k > 1) continue;
        cout << "b\n";
    }
}

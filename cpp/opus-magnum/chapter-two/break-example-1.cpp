#include <iostream>

using namespace std;

int main()
{
    int i = 7;
    while(1)
    {
        cout << "Petla, i = " << i << "\n";
        i = i - 1;
        if(i < 5)
        {
            cout << "Przerywamy te petle!\n";
            break;
        }
    }
}

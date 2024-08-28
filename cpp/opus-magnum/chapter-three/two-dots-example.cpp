#include <iostream>

using namespace std;

int k = 33;

int main()
{
    cout << "Jestem w main, k = " << k << endl;
    {
        int k = 10;
        cout << "po lokalnej definicji k = " << k
        << "\nale obiekt globalny k = " << ::k << endl;
    }
    cout << "\nPoza blokiem k = " << k << endl;
}

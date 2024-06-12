#include <iostream>

using namespace std;

int main()
{
    double przelicznik = 2.54;
    double centymetry = 0;
    int cale = 0;
    cout << "Podaj liczbe cali: ";
    cin >> cale;
    centymetry = cale * przelicznik;
    cout << cale << " - cali = " << centymetry << " centymetrow\n";
}

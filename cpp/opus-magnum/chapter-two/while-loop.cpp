#include <iostream>

using namespace std;

int main()
{
    int ile;
    cout << "Ile gwiazdek ma miec kapitan?: ";
    cin >> ile;
    cout << "\nNo to narysujmy wszystkie " << ile << ": ";

    while(ile)
    {
        cout << "*";
        ile = ile - 1;
    }

    cout << "\nTeraz zmienna ile ma wartosc " << ile << endl;
}

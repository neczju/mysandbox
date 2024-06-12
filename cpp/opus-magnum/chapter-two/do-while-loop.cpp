#include <iostream>

using namespace std;

int main()
{
    char litera;
    do{
        cout << "Napisz jakas litere: ";
        cin >> litera;
        cout << "\nNapisales: " << litera << "\n";
    }while(litera != 'K');

    cout << "Skoro napisales K to konczymy!\n";
}

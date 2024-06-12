#include <iostream>

using namespace std;

int main()
{
    cout << "Witaj uzytkowniku!\n";
    goto aaa;
    cout << "Nie widzisz tego tekstu poniewaz przeskoczylem go etykieta goto\n";
    aaa:
    cout << "Zegnaj uzyt uzytkowniku\n";
}

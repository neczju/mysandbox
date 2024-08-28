#include <iostream>

using namespace std;

int main()
{
    double szerokosc;
    decltype(szerokosc) wysokosc;

    unsigned int obj = 5;
    using typ_roboczy = decltype(obj);

    typ_roboczy zmienna1;
    typ_roboczy zmienna2;

    typ_roboczy *wskaznik;
    typ_roboczy tablica[10];
}

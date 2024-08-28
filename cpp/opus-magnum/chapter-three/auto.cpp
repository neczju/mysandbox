#include <iostream>

using namespace std;

int main()
{
    const int ctin = 10;
    constexpr int xin = 20;
    volatile int vtin = 37;

    auto h = ctin; // int h
    cout << "wartosc h po podstawieniu ctin = " << h << endl;
    h = 66;
    cout << "wartosc h po przypisaniu liczby stalej doslownej = " << h << endl;

    auto kkk = xin;
    kkk = 3;

    auto jjj = vtin;

    int in = 6;
    const auto cg = in;

    const auto ch = vtin;

    volatile auto vv = in;
    volatile auto vh = vtin;
}

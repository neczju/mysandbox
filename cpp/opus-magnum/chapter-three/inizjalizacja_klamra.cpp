#include <iostream>

using namespace std;

enum class wyliczanka { zero = 0, ene = 4, due = 10, rabe};

int globint;
double globdouble;
wyliczanka globw;

int main()
{
    int a;
    cout << "lokalny int a bez inicjalizacji = " << a << endl;

    int b{};
    cout << "lokalny int b z inicjalizacja klamrowa = " << b << endl;
    
    unsigned int c{};
    cout << "lokalny unsigned int c z inicjalizacja klamrowa = " << c << endl;

    long longinus{};
    cout << "lokalny double longinus z inicjalizacja klamrowa = " << longinus << endl;

    bool sukces{};
    cout << "lokalny bool sukces z inicjalizacja klamrowa = " << sukces << endl;

    char znak{};
    cout << "lokalny char znak z inicjalizacja klamrowa = " << znak << endl;

    wyliczanka ew{}; // bez sensu
    //cout << "lokalny wyliczanka ew z inicjalizacja klamrowa" << ew << endl;
    cout << "globalny int globint = " << globint << endl;
    cout << "globalny double globdouble = " << globdouble << endl;
    //cout << "globalny wyliczanka globw = " << globw << endl;
}

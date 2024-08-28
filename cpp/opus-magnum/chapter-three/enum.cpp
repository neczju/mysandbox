#include <cstdio>
#include <iostream>
#include <ostream>

using namespace std;

enum class Tpraca_silnikow {
    cala_wstecz = -100,
    pol_wstecz = -50,
    wolno_wstecz = -25,
    bardzo_wolno_wstecz = -5,
    stop = 0,
    bardzo_wolno_naprzod = 5,
    wolno_naprzod = 25,
    pol_naprzod = 50,
    cala_naprzod = 100
};

enum Todtwarzanie {
    play,
    stop,
    pause = 16,
    rewind_tape
};

int main(int argc, char *argv[])
{
    cout << "Kapitanie na mostku sygnalizuje telegrafem." << endl;
    Tpraca_silnikow telegraf = Tpraca_silnikow::stop;

    // czas ruszyc
    telegraf = Tpraca_silnikow::wolno_naprzod;
    // zakladamy, ze tutaj mechanik reaguje na te komende

    using Tsilniki = Tpraca_silnikow; // deklaracja wygodnego aliasu
    // kapitan decyduje, zeby plynac szybciej

    telegraf = Tsilniki::pol_naprzod;

    // Co na taka komende robi mechanik?
    cout << "Mowi mechanik. Kapitan przez telegraf rozkazal: ";
    switch (telegraf)
    {
        case Tpraca_silnikow::bardzo_wolno_naprzod:
            cout << "*bardzo wolno naprzod*" << endl;
            break;
        case Tsilniki::pol_naprzod:
            cout << "*pol naprzod*" << endl;
            break;
        case Tpraca_silnikow::cala_naprzod:
            cout << "*cala naprzod*" << endl;
            break;
    }

    int moc_silnikow = static_cast<int>(telegraf);
    cout << "co oznacza " << moc_silnikow << "% mocy silnikow" << endl;
    telegraf = Tpraca_silnikow::stop;

    enum {
        liczba_kotwic = 2,
        liczba_ladowni = 6
    };

    for(int k = 0; k < liczba_kotwic; ++k)
    {
        cout << "Opuszczamy kotwice nr " << k << " (z " << liczba_kotwic << ")" << endl;
    }
    cout << "Obserwujemy kazda z " << liczba_ladowni << " ladowni" << endl;
}

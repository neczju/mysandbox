#include <iostream>

using namespace std;

int main()
{
	cout << "Lecimy promem \"Columbia\", tu \\ bekslesz" << endl;
	cout << R"(Lecimy promem "Columbia", tu \ bekslesz)" << endl;

	cout << "C::\\transport\\nowy_projekt\\projekt1" << endl;
	cout << R"(C::\transport\nowy_projekt\projekt1)" << endl;

	cout << "linia pierwsza\nliniadruga\n";
	
	cout << R"(linia raw pierwsza
linia raw druga
)";

	cout << R"ogranicznik(Zawisza "(Czarny)" zawolal)ogranicznik" << endl;
	cout << R"##(Boleslaw "(Krzywousty)" wszedl do komnaty)##" << endl;
}

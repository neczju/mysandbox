#include <iostream>

using namespace std;

int main()
{
	cout << "Wybierz poziom sledzenia programu: [1-5]: ";
	int wybor;
	cin >> wybor;
	const int poziom_sledzenia {wybor};

	// poziom_sledzenia = 4;	// blad
	// ++poziom_sledzenia;		// blad
}

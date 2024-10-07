#include <iostream>

using namespace std;

int main()
{
	int cale;
	double centymetry;
	double przelicznik = 2.54;
	cout << "Podaj cale: ";
	cin >> cale;

	centymetry = cale * przelicznik;
	cout << cale << " cali = " << centymetry << endl;

}

#include <iostream>

using namespace std;

int main()
{
	int a = 5, b = 5, c = 5, d = 5;
	cout << "Wsteapnie\n"
		<< " a = " << a << ", b = " << b
		<< ", c = " << c << ", d = " << d << endl;

	cout << "A oto wartosc poszczegolnych wyrazen(nie mylic ze zmiennymi)\n";
	cout << "++a = " << ++a << ", b++ = " << b++
		<< ", --c = " << --c << ", d-- = " << d-- << endl;

	cout << "Po obliczeniu tych wyrazen same zmienne maja wartosci\n"
		<< "a = " << a << ", b = " << b
		<< ", c = " << c << ", d = " << d << endl;
}

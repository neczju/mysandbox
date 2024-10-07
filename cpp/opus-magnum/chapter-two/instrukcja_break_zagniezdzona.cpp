#include <iostream>

using namespace std;

int main()
{
	int zakoncz = 3;
	for (int i = 0; i < 4; i = i + 1)
	{
		for (int m = 0; m < 10; m = m + 1)
		{
			cout << "*";
			if (m > zakoncz) break;
		}
		cout << "\nKontynuujemy zewnetrzna petle for dla i = " << i << "\n";
	}
}

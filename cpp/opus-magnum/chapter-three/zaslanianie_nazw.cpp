#include <iostream>

using namespace std;

int k = 33;

int main()
{
	cout << "Jestem w main, k = " << k << "\n";
	{
		int k = 10;
		cout << "po lokalnej definicji k = " << k << endl;
	}
	cout << "Poza blokiem k = " << k << endl;
}

#include <iostream>

using namespace std;

int main()
{
	cout << "Stewardzie, ilu leci pasazerow? ";
	int ile;
	cin >> ile; 
	
	int i;
	for (i = 1; i <= ile; i = i + 1)
	{
		cout << "Pasazer nr " << i << " prosze zapiac pasy!\n";
	}
	cout << "Skoro wszyscy juz zapieli, to ladujemy.\n";
}

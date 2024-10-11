#include <iostream>

using std::cout;
using std::cin;

int main()
{
	cout << "Ilu mamy pasazerow?";
	int liczba_pasazerow;
	cin >> liczba_pasazerow;
	cout << "Mamy " << liczba_pasazerow << " pasazerow!" << std::endl; // std::endl poniewaz nie uzywam deklaracji using do std::endl
}

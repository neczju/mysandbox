#include <iostream>

int main()
{
	short int b = 0x40f2;
	short int w;
	w = b << 3;
	std::cout << "b = "  << b << std::endl;
	std::cout << "w = " << w << std::endl;
}


#include <iostream>

using namespace std;

int main()
{
	int m, i, k;
	m = 0;
	i = 0;
	while (m < 500)
	{
		while (i < 20)
		{
			for (k = 16; k < 100; k = k + 4)
			{
				cout << "k = " << k << endl;
				if (k == 32) goto po_petli;
			}
		}
	}
po_petli:
	cout <<"Po opuszczeniu wszyskich petli";
}

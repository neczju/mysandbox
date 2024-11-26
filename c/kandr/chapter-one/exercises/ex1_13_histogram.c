#include <stdio.h>

int main()
{
	int c, i;
	int nw[10];
	int w = 0;

	for (i = 0; i <= 10; ++i)
	{
		nw[i] = 0;
	}

	while ((c = getchar()) != EOF)
	{
		if (c != ' ' && c != '\n' && c != '\t')
			++nw[w];
		else
			++w;
	}

	for (i = 0; i <= 10; ++i)
	{
		if (nw[i] != 0)
		{
			for (int x = 0; x < nw[i]; ++x)
			{
				printf("-");
			}
			printf("\n");
		}
	}
}

#include <stdio.h>

int main()
{
	int c;
	int wc = 0;
	int i;
	int store[126];
	for (i = 0; i <= 126; ++i)
		store[i] = 0;

	while ((c = getchar()) != EOF)
	{
		if (c != ' ' && c != '\t' && c != '\n')
			++store[c];
		else
			++wc;
	}

	for (i = 33; i <= 126; ++i)
	{
		if (store[i] > 0)
		{
			printf("%c %d ", i, store[i]);
			for (int x = 0; x < store[i]; ++x)
				printf("-");

		printf("\n");
		}
	}
	printf("white space ");
	for (i = 0; i < wc; ++i)
		printf("-");
	printf("\n");
}

#include <stdio.h>

int main()
{
	int c;
	int is_s = 0;
	while ((c = getchar()) != EOF)
	{
		if (is_s == 0 && c == ' ') {
			putchar(c);
			is_s = 1;
		}
		if (is_s == 1 && c == ' ')
			;
		else {
			putchar(c);
			is_s = 0;
		}
	}
}

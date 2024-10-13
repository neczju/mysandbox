#include <stdio.h>
#define MAXSIZE 1000

void reverse(char s[]);
int get_line(char s[]);

int main()
{
	char line[MAXSIZE];
	while (get_line(line))
	{
		reverse(line);
		printf("\n");
	}
	return 0;
}

void reverse(char s[])
{
	int i;
	int r = 0;

	for (i = MAXSIZE; i >= 0; --i)
	{
		if (s[i] == '\0')
			r = 1;
		if (r == 1)
			putchar(s[i]);
	}
}
int get_line(char s[])
{
	int c, i;
	for (i = 0; i < MAXSIZE - 1; ++i)
		s[i] = 0;

	for (i = 0; i < MAXSIZE - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
	{
		s[i] = c;
		if (c == '\n') {
			++i;
			s[i] = '\0';
		}

	}
	return i;
}


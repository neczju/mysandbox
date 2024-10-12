#include <stdio.h>
#define MAXSIZE 1000

int get_line(char s[], int lim);
void remove_wc(char to[], char from[]);

int main()
{
	char line[MAXSIZE];
	char line_mod[MAXSIZE];
	while (get_line(line, MAXSIZE))
	{
		remove_wc(line_mod, line);
	}
}

int get_line(char s[], int lim)
{
	int c, i;
	for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
		s[i] = c;
	if (c == '\n') {
		s[i] = c;
		++i;
	}
	s[i] = '\0';
	return i;
}

void remove_wc(char to[], char from[])
{
	int i;
	i = 0;
	while ((to[i] = from[i]) != '\0')
		++i;
}

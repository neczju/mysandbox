#include <stdio.h>
#define MAXLINE 1000

int get_line(char line[], int maxline);

int main()
{
	int len; /* dlugosc biezacego wiersza */
	char line[MAXLINE];

	while ((len = get_line(line, MAXLINE)) > 0)
		printf("%s", line);
	return 0;
}

/* getline: pobiera wiersz do tablicy s, zwraca dlugosc */
int get_line(char s[], int lim)
{
	int c, i;

	for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i) /* powtarza dopoki nie napotka znaku nowego wiersza lub przekroczy limit */
		s[i] = c;
	if (c == '\n') {
		s[i] = c;
		++i;
	}
	s[i] = '\0';
	return i;
}

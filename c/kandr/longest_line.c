#include <stdio.h>
#define MAXLINE 1000

int get_line(char line[], int maxline);
void copy(char to[], char from[]);

int main()
{
	int len; /* dlugosc biezacego wiersza */
	int max; /* najwieksza znana dlugosc */
	char line[MAXLINE];
	char longest[MAXLINE];

	max = 0;
	while ((len = get_line(line, MAXLINE)) > 0)
		if (len > max) { /* wyszukanie najdluzszego wiersza */
			max = len;
			copy(longest, line);
		}
	if (max > 0)
		printf("%s", longest);
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

/* copy: kopiuje from do to, zaklada wystarczajacy rozmiar */
void copy(char to[], char from[])
{
	int i;

	i = 0;
	while ((to[i] = from[i]) != '\0')
		++i;
}

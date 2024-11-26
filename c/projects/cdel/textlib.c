/* textlib.c
 *
 * simple text operation library  
 */

#include <stdio.h>

#define MAXSIZE 1000

/* removes given character from array */
void TL_RemoveChar(char s[], char out[], char c)
{
	int i, z;

	for (i = 0; i < MAXSIZE - 1; ++i)
		out[i] = 0;

	for (i = 0, z = 0; i < MAXSIZE - 1; ++i)
		if (s[i] != c) {
			out[z] = s[i];
			++z;
		}
}

/* replaces first character argument form array with second character argument */
void TL_ReplaceChar(char s[], char c, char ic)
{
	int i;

	for (i = 0; i < MAXSIZE - 1; ++i)
	{
		if (s[i] == c)
			s[i] = ic;
	}
}

/* initializes line of text to an array */
void TL_GetLine(char s[])
{
	int i, c;

	for (i = 0; i < MAXSIZE - 1; ++i)
		s[i] = 0;

	for (i = 0; i < MAXSIZE - 1 && (c = getchar()) != '\n'; ++i)
		s[i] = c;
}

void TL_ReverseLine(char s[], char out[])
{
	int i, h;

	for (i = 0; i < MAXSIZE - 1; ++i)
		out[i] = 0;

	for (i = MAXSIZE, h = 0; i >= 0; --i, ++h)
		if (s[i])
			out[h] = s[i];
}

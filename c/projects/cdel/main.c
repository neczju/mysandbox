/* main.c
 *
 * simple text operation program 
 */

#include <stdio.h>
#include "textlib.h"

int main(void)
{
	char line[MAXSIZE];
	char out[MAXSIZE];
	char c, ic;
	int op;

	printf("type text: ");
	TL_GetLine(line);

	//printf("what operation you want do:\n");
	//printf("1. remove character\n");
	//printf("2. replace character\n");

	//op = getchar(); getchar();
	/* switch (op)
	{
		case '1':
			printf("type character to delete from text: ");
			c = getchar();		
			TL_RemoveChar(line, out, c);
			printf("%s\n", out);
			break;
		case '2':
			printf("type character you want to change: ");
			c = getchar(); getchar();
			printf("type character you want to place: ");
			ic = getchar();
			TL_ReplaceChar(line, c, ic);
			printf("%s\n", line);
			break;
			
	} */
	TL_ReverseLine(line, out);
	printf("output: %s\n", out);
	return 0;
}

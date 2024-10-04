#include <stdio.h>

int main()
{
	int c, wc;
	wc = 0;
	while ((c = getchar()) != EOF) {
		if(c == ' ')
			++wc;
		if(c == '\t')
			++wc;
		if(c == '\n')
			++wc;	
	}
	printf("%d\n", wc);
}

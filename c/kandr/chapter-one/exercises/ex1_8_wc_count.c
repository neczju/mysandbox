#include <stdio.h>

int main()
{
	int c;
	int spaces = 0;
	int tabs = 0;
	int nl = 0;
	while ((c = getchar()) != EOF) {
		if(c == ' ')
			++spaces;
		if(c == '\t')
			++tabs;
		if(c == '\n')
			++nl;	
	}
	printf("spaces: %d, tabs: %d, new lines: %d\n", spaces, tabs, nl);
}

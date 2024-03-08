#include <stdio.h>

int main()
{
	char str[6] = { 0, };
	puts("You have to do count down.");
	printf("(5 -> 1)\n > ");
	fflush(stdout);
	scanf("%s", str);
	if (strcmp(str, "\x05\x04\x03\x02\x01")) 
		exit(0);
	system("cat flag");
}

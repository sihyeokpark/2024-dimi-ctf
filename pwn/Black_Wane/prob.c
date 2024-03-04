#include <stdio.h>
#include <string.h>

void get_shell() {
	system("/bin/sh");
}

int main() {
	char buf[8];
	puts("Hello, my name is Wane!");
	puts("I cracked many program.");
	printf("Do you want to connect me?\n(yes/no) >> ");
	fflush(stdout);
	scanf("%s", buf);
	if (!strcmp(buf, "yes") ) {
		puts("Oh, I got it.");
		puts("Here is my discord >> __readfsqword");
		exit(0);
	}
	else {
		puts("Ok.");
		puts("I remebered ur choice");
		puts("See u soon...");
	}
	get_shell();
	return 0;
}

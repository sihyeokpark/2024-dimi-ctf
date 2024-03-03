#include <stdio.h>

int main() {
	puts("You ready?");
	puts("Let's go!!");
	fflush(stdout);
	system("/bin/sh");
	return 0;
}

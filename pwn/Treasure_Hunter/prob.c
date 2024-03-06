#include <stdio.h>

int main() {
	puts("You ready?");
	puts("Let's go!!");
	fflush(stdout);
	write(0, 9, "\x61\x2d\x20\x73\x6c\x20\x45\x53\x55");
	system("/bin/sh");
	return 0;
}

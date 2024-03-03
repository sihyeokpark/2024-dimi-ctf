#include <stdio.h>
#include <unistd.h>

int main() {
	char buf[0x10];
	char ver[0x10] = {0,};
	puts("make BOF");
	printf(" > ");
	fflush(stdout);
	read(0, buf, 0x100);
	if (ver[4]) {
		puts("WoW");
		sleep(1);
		puts("You made Brain Over Flow");
		sleep(1);
		puts("After bof, ver is like this.");
		printf("%s", ver);
		fflush(stdout);
		sleep(1);
		puts("Here is flag, Bye Bye");
		system("cat flag");
		return 0;
	}
	puts("You failed!");
	return 0;
}

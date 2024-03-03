#include <stdio.h>

int main() {
	char command[0x10];
	puts("I can do everything.");
	printf("What do you want to do? > ");
	fflush(stdout);
	scanf("%s", command);
	puts("Ok, I'll do that for you!");
	system(command);
	return 0;
}

#include <stdio.h>

void clear(void) {
	system("clear");
}

int main() {
	void (*ptr)(void);

	puts("This can do Bakkuachigi.");
	puts("What do you want to Bakkuachigi?");
	printf("first one > ");
	fflush(stdout);
	scanf("%s", &ptr);
	printf("Second one > ");
	fflush(stdout);
	scanf("%s", ptr);
	
	puts("/bin/sh"); // system("/bin/sh");

	return 0;
}

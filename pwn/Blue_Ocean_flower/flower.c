#include <stdio.h>
#include <string.h>

void flag() {
	system("cat flag");
}

int main() {
	char resp[0x10];
	char location[0x10] = "field";
	puts("I am Blue Ocean Flower");
	puts("I want to go to Ocean!");
	printf("Please take me to the Ocean...\n > ");
	fflush(stdout);
	read(0, resp, 0x100);
	if (!strcmp(location, "ocean")) {
		puts("Thank you very much!");
		puts("This is present for You!");
		flag();
	}
	else {
		puts("... here isn't ocean..");
	}
	return 0;
}	

#include <stdio.h>
#include <string.h>
#include <time.h>

#define N 3

int main() {
	int choice = 0;
	char cmd[20] = {0, };
	char filter[N][10] = {"flag", "sh", "/"};
	puts("This a small machine.");
	sleep(1);
	printf("If u bring me to cafe, I'll do onething for u > ");
	fflush(stdout);
	scanf("%d", &choice);
	if (choice == 0xcafe) {
		puts("I need some coffee....");
		printf("What should I do?\n > ");
		fflush(stdout);
		read(0,cmd,19);
		for (int i = 0; i < N; i ++ ) {
			if (strstr(cmd, filter[i])) {
				puts("NOPE");
				return 0;
			}
		}
		system(cmd);
	}
	puts("NO, NO, NO, No, No, No, No!!");
	return 0;
}

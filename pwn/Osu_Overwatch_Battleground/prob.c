#include <stdio.h>
#include <string.h>

int main() {
	char osu[4] = {0,};
	char game[3][0x10];
	int index;
	puts("what game do you play?");
	printf("1. lol\n2. bag\n3. obch..\n?. osu?\nType your one pick > ");
	fflush(stdout);
	scanf("%d", &index);
	printf("Type your game name > ");
	fflush(stdout);
	scanf("%s", game[index]);
	printf("Wow, U play %s!!", game[index]);
	if (strcmp(osu, "osu")) {
		puts("YEEEEEEESSSS!");
		puts("Osu is the best Game in the world!!!");
		puts("Here is flag.");
		fflush(stdout);
		system("cat flag");
	}
	else {
		puts("Well, But Osu is best Game in the world, LOL");
		puts("Download Osu and Play it.");
	}
}

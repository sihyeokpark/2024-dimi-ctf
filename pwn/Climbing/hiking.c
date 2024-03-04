#include <stdio.h>
#include <unistd.h>

char shell[8] = "/bin/sh";

void gadget() {
	asm(".intel_syntax noprefix\n"
			"pop rdi\n"
			"ret\n"
			".att_syntax \n"
			:
			:
			: "rdi"
			);
}

void clear() {
	system("clear");
}

void menu() {
	puts("1. Climb with Rope");
	puts("2. Go to the other way");
	puts("3. Descend this mountain");
	printf(" > ");
}

void ROPe() {
	char yell[0x20] = "Yahoooo!";
	puts("climbing....");
	sleep(1);
	puts("Kiki successfully reached the top of mountain!");
	printf("What sentence do you want to shout out? > ");
	fflush(stdout);
	read(0, yell, 0x200);
	printf("%s!!", yell);
}

void Turn() {
	puts("The other way takes 1hour more than this route.");
	sleep(0.5);
	puts("Kiki reached to the top of this mountain.");
	puts("But you are too exhausted to shout something...");
}

void Descend() {
	puts("Kiki decided to descend this mountain.");
	puts("It was very sensible choice!");
	exit(0);
	
}

int main() {
	int choice;
	puts("The clif is too high.");
	puts("How can I climb this wall?");
	menu();
	fflush(stdout);
	scanf("%d", &choice);
        switch(choice) {
		case 1: ROPe(); break;
		case 2: Turn(); break;
		case 3: Descend(); break;
		default : puts("Can't do that...");
	}
	return 0;
}

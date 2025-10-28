#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_CMD 100
#define MAX_ARGS 10

int main() {
    char command[MAX_CMD];
    char *args[MAX_ARGS];
    char *token;

    while (1) {
        printf("myshell> ");
        fflush(stdout);

        if (fgets(command, MAX_CMD, stdin) == NULL) {
            printf("\n");
            break;
        }

        command[strcspn(command, "\n")] = '\0'; // remove newline

        if (strcmp(command, "exit") == 0)
            break;

        if (strlen(command) == 0)
            continue;

        int i = 0;
        token = strtok(command, " ");
        while (token != NULL && i < MAX_ARGS - 1) {
            args[i++] = token;
            token = strtok(NULL, " ");
        }
        args[i] = NULL;

        pid_t pid = fork();
        if (pid == 0) {
            execvp(args[0], args);
            printf("Command not found: %s\n", args[0]);
            exit(1);
        } else if (pid > 0) {
            wait(NULL);
        } else {
            perror("fork");
        }
    }

    return 0;
}

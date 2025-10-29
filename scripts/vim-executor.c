#include <stdio.h>
#include <stdlib.h> // exit(), system()
#include <string.h> // snprintf()

int main(int argc, char *argv[]) {
    FILE *fp;
    int c;
    char command_buffer[2048];

    // 1. Check command-line arguments
    // Both argv[1] (vim script) and argv[2] (output file) are required
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <vim script> <output filename>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    // 2. Open file (write target is argv[2])
    fp = fopen(argv[2], "w");
    if (fp == NULL) {
        perror("Cannot open file (write)");
        exit(EXIT_FAILURE);
    }

    // 3. Read from stdin and write to argv[2]
    while ((c = fgetc(stdin)) != EOF) {
        fputc(c, fp);
    }

    // 4. Close the output file
    fclose(fp);

    // 5. Build the vim command
    // Construct the string with snprintf to avoid buffer overrun
    snprintf(command_buffer, sizeof(command_buffer), 
      "/usr/bin/vim -es -u NONE -X -Z -n -f --not-a-term %s +vi < %s", argv[2], argv[1]);

    // 6. Launch vim
    // printf("Command to execute: %s\n", command_buffer); // for debugging
    system(command_buffer); // Execute the command and wait for vim to exit
    
    // 7. After vim exits, reopen argv[2] in read mode
    fp = fopen(argv[2], "r");
    if (fp == NULL) {
        perror("Cannot open file (read)");
        exit(EXIT_FAILURE);
    }

    // 8. Write the file contents to standard output (stdout)
    while ((c = fgetc(fp)) != EOF) {
        fputc(c, stdout); // write one character at a time to stdout
    }

    // 9. Close the read file
    fclose(fp);

    return EXIT_SUCCESS; // success
}
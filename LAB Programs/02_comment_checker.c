/* 
 * Experiment 2: Lexical Analyzer to check whether a given line is a comment or not
 * Checks both // and /* */ style comments
 */
#include <stdio.h>
#include <string.h>

int main() {
    char line[500];

    printf("Enter a line of code: ");
    fgets(line, sizeof(line), stdin);
    line[strcspn(line, "\n")] = '\0';

    // Skip leading whitespace
    char *ptr = line;
    while (*ptr == ' ' || *ptr == '\t') ptr++;

    if (strncmp(ptr, "//", 2) == 0) {
        printf("Result: Single-line comment (// style)\n");
    } else if (strncmp(ptr, "/*", 2) == 0) {
        int len = strlen(ptr);
        if (ptr[len - 1] == '/' && len >= 4 && ptr[len - 2] == '*') {
            // Check if it ends with */
            // Actually we need to check if there's */ somewhere
            char *end = strstr(ptr + 2, "*/");
            if (end != NULL) {
                printf("Result: Multi-line comment (/* */ style)\n");
            } else {
                printf("Result: Incomplete multi-line comment (starts with /* but no */)\n");
            }
        } else {
            char *end = strstr(ptr + 2, "*/");
            if (end != NULL) {
                printf("Result: Multi-line comment (/* */ style)\n");
            } else {
                printf("Result: Incomplete multi-line comment (starts with /* but no */)\n");
            }
        }
    } else {
        printf("Result: Not a comment\n");
    }

    return 0;
}
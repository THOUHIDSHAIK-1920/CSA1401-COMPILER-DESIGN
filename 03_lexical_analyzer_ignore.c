/* 
 * Experiment 3: Lexical Analyzer that ignores redundant spaces, tabs, newlines, and comments
 */
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    FILE *fp;
    char filename[100], ch;

    printf("Enter source file name: ");
    scanf("%s", filename);
    fp = fopen(filename, "r");
    if (!fp) {
        printf("Error opening file!\n");
        return 1;
    }

    printf("\nOutput (after removing spaces, tabs, newlines, and comments):\n");
    printf("----------------------------------------------------------\n");

    while ((ch = fgetc(fp)) != EOF) {
        // Ignore spaces, tabs, newlines
        if (ch == ' ' || ch == '\t' || ch == '\n')
            continue;

        // Ignore single-line comments
        if (ch == '/') {
            int next = fgetc(fp);
            if (next == '/') {
                while ((ch = fgetc(fp)) != '\n' && ch != EOF);
                continue;
            } else if (next == '*') {
                while ((ch = fgetc(fp)) != EOF) {
                    if (ch == '*') {
                        if ((ch = fgetc(fp)) == '/')
                            break;
                    }
                }
                continue;
            } else {
                ungetc(next, fp);
                putchar(ch);
            }
        } else {
            putchar(ch);
        }
    }

    fclose(fp);
    printf("\n");
    return 0;
}
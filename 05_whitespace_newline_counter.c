/* 
 * Experiment 5: Lexical Analyzer to find the number of whitespaces and newline characters
 */
#include <stdio.h>

int main() {
    FILE *fp;
    char filename[100], ch;
    int whitespaces = 0, newlines = 0, tabs = 0;

    printf("Enter file name: ");
    scanf("%s", filename);
    fp = fopen(filename, "r");
    if (!fp) {
        printf("Error opening file!\n");
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF) {
        if (ch == ' ')
            whitespaces++;
        else if (ch == '\t')
            tabs++;
        else if (ch == '\n')
            newlines++;
    }

    fclose(fp);

    printf("\nResults:\n");
    printf("--------\n");
    printf("Spaces: %d\n", whitespaces);
    printf("Tabs: %d\n", tabs);
    printf("Newlines: %d\n", newlines);
    printf("Total whitespace characters: %d\n", whitespaces + tabs + newlines);

    return 0;
}
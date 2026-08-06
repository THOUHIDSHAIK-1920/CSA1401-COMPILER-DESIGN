/* 
 * Experiment 15: Lexical Analyzer to scan and count characters, words, and lines in a file
 */
#include <stdio.h>
#include <ctype.h>

int main() {
    FILE *fp;
    char filename[100], ch;
    int chars = 0, words = 0, lines = 0;
    int in_word = 0;

    printf("Enter file name: ");
    scanf("%s", filename);
    fp = fopen(filename, "r");
    if (!fp) {
        printf("Error opening file!\n");
        return 1;
    }

    while ((ch = fgetc(fp)) != EOF) {
        chars++;
        
        if (ch == '\n')
            lines++;
        
        if (isspace(ch)) {
            in_word = 0;
        } else {
            if (!in_word) {
                words++;
                in_word = 1;
            }
        }
    }

    fclose(fp);

    printf("\nResults:\n");
    printf("--------\n");
    printf("Characters: %d\n", chars);
    printf("Words: %d\n", words);
    printf("Lines: %d\n", lines);

    return 0;
}
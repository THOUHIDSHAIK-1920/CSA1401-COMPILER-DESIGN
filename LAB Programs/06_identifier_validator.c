/* 
 * Experiment 6: Lexical Analyzer to test whether a given identifier is valid or not
 */
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char id[100];
    int i, valid = 1;

    printf("Enter an identifier: ");
    scanf("%s", id);

    // Check if first character is a letter or underscore
    if (!(isalpha(id[0]) || id[0] == '_')) {
        valid = 0;
    } else {
        // Check remaining characters
        for (i = 1; id[i] != '\0'; i++) {
            if (!(isalnum(id[i]) || id[i] == '_')) {
                valid = 0;
                break;
            }
        }
    }

    // Check if it's a keyword
    char *keywords[] = {"auto", "break", "case", "char", "const", "continue", "default",
                        "do", "double", "else", "enum", "extern", "float", "for", "goto",
                        "if", "int", "long", "register", "return", "short", "signed",
                        "sizeof", "static", "struct", "switch", "typedef", "union",
                        "unsigned", "void", "volatile", "while"};
    for (i = 0; i < 32; i++) {
        if (strcmp(id, keywords[i]) == 0) {
            valid = 0;
            printf("'%s' is a keyword, cannot be used as identifier.\n", id);
            return 0;
        }
    }

    if (valid)
        printf("'%s' is a VALID identifier.\n", id);
    else
        printf("'%s' is NOT a valid identifier.\n", id);

    return 0;
}
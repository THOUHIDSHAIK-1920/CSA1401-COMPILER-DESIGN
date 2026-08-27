/* 
 * Experiment 1: Lexical Analyzer to identify identifiers, constants, and operators
 * Ignores redundant spaces, tabs, new lines, and comments
 */
#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define MAX_ID_LEN 32

int isOperator(char ch) {
    char ops[] = "+-*/%=<>!&|^~";
    for (int i = 0; ops[i]; i++)
        if (ch == ops[i]) return 1;
    return 0;
}

int isKeyword(char *str) {
    char *keywords[] = {"auto", "break", "case", "char", "const", "continue", "default",
                        "do", "double", "else", "enum", "extern", "float", "for", "goto",
                        "if", "int", "long", "register", "return", "short", "signed",
                        "sizeof", "static", "struct", "switch", "typedef", "union",
                        "unsigned", "void", "volatile", "while"};
    for (int i = 0; i < 32; i++)
        if (strcmp(str, keywords[i]) == 0) return 1;
    return 0;
}

int main() {
    FILE *fp;
    char filename[100], ch, buffer[MAX_ID_LEN];
    int i;

    printf("Enter source file name: ");
    scanf("%s", filename);
    fp = fopen(filename, "r");
    if (!fp) {
        printf("Error opening file!\n");
        return 1;
    }

    printf("\nTOKENS:\n");
    printf("-------\n");

    while ((ch = fgetc(fp)) != EOF) {
        // Ignore spaces, tabs, newlines
        if (ch == ' ' || ch == '\t' || ch == '\n')
            continue;

        // Ignore single-line comments
        if (ch == '/' && (ch = fgetc(fp)) == '/') {
            while ((ch = fgetc(fp)) != '\n' && ch != EOF);
            continue;
        }
        // Ignore multi-line comments
        if (ch == '*' && (ch = fgetc(fp)) == '/') {  // Actually handling /* ... */
            // We already read '/', then '*', now check for '/'
            // Actually rewind: we read '/', then '*', skip until '*/'
            while ((ch = fgetc(fp)) != EOF) {
                if (ch == '*') {
                    if ((ch = fgetc(fp)) == '/')
                        break;
                }
            }
            continue;
        }
        // Rewind if we read '*' after '/' and it wasn't start of comment
        // Actually simpler: handle comments properly
        // Let me redo - the above logic is wrong for /* */
        // We need to handle the /* case when we see '/' and then '*'
        // Let me just use ungetc properly
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
                // Fall through to check as operator
                if (isOperator('/')) {
                    printf("Operator: /\n");
                    continue;
                }
            }
        }

        // Identifier or Keyword
        if (isalpha(ch) || ch == '_') {
            i = 0;
            while (isalnum(ch) || ch == '_') {
                if (i < MAX_ID_LEN - 1) buffer[i++] = ch;
                ch = fgetc(fp);
            }
            buffer[i] = '\0';
            ungetc(ch, fp);
            if (isKeyword(buffer))
                printf("Keyword: %s\n", buffer);
            else
                printf("Identifier: %s\n", buffer);
            continue;
        }

        // Constant (number)
        if (isdigit(ch)) {
            i = 0;
            while (isdigit(ch)) {
                buffer[i++] = ch;
                ch = fgetc(fp);
            }
            buffer[i] = '\0';
            ungetc(ch, fp);
            printf("Constant: %s\n", buffer);
            continue;
        }

        // String constants
        if (ch == '"') {
            i = 0;
            buffer[i++] = ch;
            while ((ch = fgetc(fp)) != EOF) {
                buffer[i++] = ch;
                if (ch == '"') break;
                if (ch == '\\') buffer[i++] = fgetc(fp);
            }
            buffer[i] = '\0';
            printf("String: %s\n", buffer);
            continue;
        }

        // Character constant
        if (ch == '\'') {
            i = 0;
            buffer[i++] = ch;
            while ((ch = fgetc(fp)) != EOF) {
                buffer[i++] = ch;
                if (ch == '\'') break;
                if (ch == '\\') buffer[i++] = fgetc(fp);
            }
            buffer[i] = '\0';
            printf("Char Const: %s\n", buffer);
            continue;
        }

        // Operators
        if (isOperator(ch)) {
            printf("Operator: %c\n", ch);
            continue;
        }

        // Special symbols / separators
        if (ch == '(' || ch == ')' || ch == '{' || ch == '}' || 
            ch == '[' || ch == ']' || ch == ';' || ch == ',') {
            printf("Separator: %c\n", ch);
            continue;
        }
    }

    fclose(fp);
    return 0;
}
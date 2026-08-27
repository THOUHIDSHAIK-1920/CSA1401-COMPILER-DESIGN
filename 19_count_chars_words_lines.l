%{
/*
 * Experiment 19: LEX program to count characters, lines & words from a .c file
 */
#include <stdio.h>
int chars = 0, words = 0, lines = 0;
%}

%%
[a-zA-Z0-9_]+  { words++; chars += strlen(yytext); }
[ \t]+          { chars += strlen(yytext); }
\n              { lines++; chars++; }
.               { chars++; }
%%

int yywrap() { return 1; }

int main(int argc, char *argv[]) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            printf("Error opening file %s\n", argv[1]);
            return 1;
        }
    }
    yylex();
    printf("\n--- Results ---\n");
    printf("Characters: %d\n", chars);
    printf("Words: %d\n", words);
    printf("Lines: %d\n", lines);
    return 0;
}
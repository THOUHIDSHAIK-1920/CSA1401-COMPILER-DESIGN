%{
/*
 * Experiment 20 (continued): LEX program to count Macros and Header files
 */
#include <stdio.h>
int macros = 0, headers = 0;
%}

%%
^#define.*       { macros++; }
^#include.*     { headers++; }
.|\n            { /* ignore */ }
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
    printf("Number of Macros defined: %d\n", macros);
    printf("Number of Header files included: %d\n", headers);
    return 0;
}
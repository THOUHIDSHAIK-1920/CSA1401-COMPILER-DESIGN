%{
/*
 * Experiment 20: LEX program to print all constants in a C source program file
 */
#include <stdio.h>
%}

%%
[0-9]+(\.[0-9]+)?  { printf("Constant: %s\n", yytext); }
\"[^"]*\"           { printf("String: %s\n", yytext); }
\'[^']*\'           { printf("Char Constant: %s\n", yytext); }
.|\n                { /* ignore everything else */ }
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
    return 0;
}
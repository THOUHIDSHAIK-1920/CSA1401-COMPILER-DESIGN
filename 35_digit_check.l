%{
/*
 * Experiment 35: LEX program to check whether the given input is a digit or not
 */
#include <stdio.h>
%}

%%
[0-9]      { printf("'%s' is a DIGIT.\n", yytext); }
.          { printf("'%s' is NOT a digit.\n", yytext); }
\n         { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a character: ");
    yylex();
    return 0;
}
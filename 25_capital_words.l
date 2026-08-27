%{
/*
 * Experiment 25: LEX program to identify capital words from the given input
 */
#include <stdio.h>
%}

%%
[A-Z][A-Z ]+  { printf("Capital Word: %s\n", yytext); }
[A-Z]          { printf("Capital Letter: %s\n", yytext); }
.|\n           { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter text: ");
    yylex();
    return 0;
}
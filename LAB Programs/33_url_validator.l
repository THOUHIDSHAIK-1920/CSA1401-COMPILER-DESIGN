%{
/*
 * Experiment 33: LEX program to validate a URL
 */
#include <stdio.h>
%}

%%
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)  { printf("Valid URL: %s\n", yytext); }

[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}  { printf("Valid URL: %s\n", yytext); }

.|\n                            { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a URL: ");
    yylex();
    return 0;
}
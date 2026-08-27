%{
/*
 * Experiment 26: LEX program to check if an email address is valid
 */
#include <stdio.h>
%}

%%
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}  { printf("Valid Email: %s\n", yytext); }
[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]*                  { printf("Invalid Email: %s\n", yytext); }
.|\n                                               { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter email address: ");
    yylex();
    return 0;
}
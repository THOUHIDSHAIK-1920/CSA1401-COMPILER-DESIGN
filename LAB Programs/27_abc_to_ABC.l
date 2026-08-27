%{
/*
 * Experiment 27: LEX program to convert substring "abc" to "ABC" from given input string
 */
#include <stdio.h>
%}

%%
abc  { printf("ABC"); }
.    { printf("%s", yytext); }
\n   { printf("\n"); }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a string: ");
    yylex();
    printf("\n");
    return 0;
}
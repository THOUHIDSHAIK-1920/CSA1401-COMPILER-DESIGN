%{
/*
 * Experiment 36: LEX program to implement basic mathematical operations
 */
#include <stdio.h>
%}

%%
[0-9]+   { printf("Number: %s\n", yytext); }
"+"      { printf("Operator: PLUS\n"); }
"-"      { printf("Operator: MINUS\n"); }
"*"      { printf("Operator: MULTIPLY\n"); }
"/"      { printf("Operator: DIVIDE\n"); }
"="      { printf("Operator: EQUALS\n"); }
.|\n     { /* ignore whitespace and others */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a mathematical expression: ");
    yylex();
    return 0;
}
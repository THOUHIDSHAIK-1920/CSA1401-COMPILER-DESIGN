%{
/*
 * Experiment 32: LEX program to identify and count positive and negative numbers
 */
#include <stdio.h>
int positive = 0, negative = 0;
%}

%%
-[0-9]+(\.[0-9]+)?  { negative++; printf("Negative Number: %s\n", yytext); }
[0-9]+(\.[0-9]+)?   { positive++; printf("Positive Number: %s\n", yytext); }
.|\n                 { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter numbers: ");
    yylex();
    printf("\n--- Summary ---\n");
    printf("Positive numbers: %d\n", positive);
    printf("Negative numbers: %d\n", negative);
    return 0;
}
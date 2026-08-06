%{
/*
 * Experiment 28: LEX program to check whether a mobile number is valid or not
 * Valid: 10-digit number starting with 6,7,8,9
 */
#include <stdio.h>
%}

%%
[6-9][0-9]{9}  { printf("Valid Mobile Number: %s\n", yytext); }
[0-9]+         { printf("Invalid Mobile Number: %s\n", yytext); }
.|\n           { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a mobile number: ");
    yylex();
    return 0;
}
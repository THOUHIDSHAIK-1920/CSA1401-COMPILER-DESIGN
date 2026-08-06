%{
/*
 * Experiment 34: LEX program to validate Date of Birth (DD/MM/YYYY or DD-MM-YYYY format)
 */
#include <stdio.h>
%}

%%
(0[1-9]|[12][0-9]|3[01])[/-](0[1-9]|1[012])[/-](19|20)[0-9]{2}  { printf("Valid DOB: %s\n", yytext); }

[0-9]+[/-][0-9]+[/-][0-9]+  { printf("Invalid DOB: %s\n", yytext); }

.|\n                           { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter Date of Birth (DD/MM/YYYY): ");
    yylex();
    return 0;
}
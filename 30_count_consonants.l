%{
/*
 * Experiment 30: LEX program to count the number of consonants in a given sentence
 */
#include <stdio.h>
int consonants = 0;
%}

%%
[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]  { consonants++; }
.|\n                                             { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a sentence: ");
    yylex();
    printf("Number of consonants: %d\n", consonants);
    return 0;
}
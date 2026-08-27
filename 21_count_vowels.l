%{
/*
 * Experiment 21: LEX program to count the number of vowels in a given sentence
 */
#include <stdio.h>
int vowels = 0;
%}

%%
[aeiouAEIOU]  { vowels++; }
.|\n          { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a sentence: ");
    yylex();
    printf("Number of vowels: %d\n", vowels);
    return 0;
}
%{
/*
 * Experiment 37: LEX program to count the frequency of a given word in a sentence
 */
#include <stdio.h>
#include <string.h>
char target[100];
int count = 0;
%}

%%
[a-zA-Z]+  { if (strcmp(yytext, target) == 0) count++; }
.|\n       { /* ignore */ }
%%

int yywrap() { return 1; }

int main(int argc, char *argv[]) {
    printf("Enter the word to search: ");
    scanf("%s", target);
    printf("Enter the sentence: ");
    yylex();
    printf("Frequency of '%s': %d\n", target, count);
    return 0;
}
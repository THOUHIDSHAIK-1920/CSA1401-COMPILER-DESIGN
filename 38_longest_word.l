%{
/*
 * Experiment 38: LEX program to find the length of the longest word
 */
#include <stdio.h>
#include <string.h>
int max_len = 0;
char longest[100] = "";
%}

%%
[a-zA-Z]+  { 
    int len = strlen(yytext);
    if (len > max_len) {
        max_len = len;
        strcpy(longest, yytext);
    }
}
.|\n       { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter a sentence: ");
    yylex();
    printf("Longest word: '%s'\n", longest);
    printf("Length: %d\n", max_len);
    return 0;
}
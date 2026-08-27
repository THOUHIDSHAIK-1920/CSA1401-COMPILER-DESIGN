%{
/*
 * Experiment 39: LEX program to replace a word with another word in a file
 */
#include <stdio.h>
#include <string.h>
char old_word[100], new_word[100];
%}

%%
[a-zA-Z]+  { 
    if (strcmp(yytext, old_word) == 0)
        printf("%s", new_word);
    else
        printf("%s", yytext);
}
.          { printf("%s", yytext); }
\n         { printf("\n"); }
%%

int yywrap() { return 1; }

int main(int argc, char *argv[]) {
    printf("Enter word to replace: ");
    scanf("%s", old_word);
    printf("Enter new word: ");
    scanf("%s", new_word);
    printf("Enter text (Ctrl+Z to end):\n");
    yylex();
    return 0;
}
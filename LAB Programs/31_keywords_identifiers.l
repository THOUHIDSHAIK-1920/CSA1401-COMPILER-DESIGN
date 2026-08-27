%{
/*
 * Experiment 31: LEX program to separate keywords and identifiers
 */
#include <stdio.h>
%}

%%
"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|"int"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"void"|"volatile"|"while"  { printf("KEYWORD: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*  { printf("IDENTIFIER: %s\n", yytext); }

.|\n                     { /* ignore */ }
%%

int yywrap() { return 1; }

int main() {
    printf("Enter code: ");
    yylex();
    return 0;
}
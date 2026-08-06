%{
/*
 * Experiment 40: FLEX program to perform token separation for a given C program
 */
#include <stdio.h>
%}

%%
"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|"int"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"void"|"volatile"|"while"  { printf("Keyword: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]*  { printf("Identifier: %s\n", yytext); }

[0-9]+(\.[0-9]+)?       { printf("Number: %s\n", yytext); }

\"[^"]*\"               { printf("String: %s\n", yytext); }

"+"|"-"|"*"|"/"|"%"|"="|"=="|"!="|"<"|">"|"<="|">="|"&&"|"||"|"!"|"&"|"|"|"~"|"^"|"<<"|">>"|"++"|"--"|"+="|"-="  { printf("Operator: %s\n", yytext); }

"("|")"|"{"|"}"|"["|"]"|";"|","  { printf("Separator: %s\n", yytext); }

"//"[^\n]*      { printf("Comment: %s\n", yytext); }

[ \t\n]+        { /* ignore whitespace */ }
.               { /* ignore */ }
%%

int yywrap() { return 1; }

int main(int argc, char *argv[]) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            printf("Error: Cannot open file %s\n", argv[1]);
            return 1;
        }
    }
    printf("\n--- TOKEN SEPARATION ---\n\n");
    yylex();
    return 0;
}
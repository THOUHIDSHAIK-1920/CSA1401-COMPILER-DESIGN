%{
/*
 * Experiment 22: LEX program to print all HTML tags in an input file
 */
#include <stdio.h>
%}

%%
"<"[^>]*">"  { printf("HTML Tag: %s\n", yytext); }
.|\n         { /* ignore */ }
%%

int yywrap() { return 1; }

int main(int argc, char *argv[]) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            printf("Error opening file %s\n", argv[1]);
            return 1;
        }
    }
    yylex();
    return 0;
}
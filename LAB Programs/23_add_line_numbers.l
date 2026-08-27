%{
/*
 * Experiment 23: LEX program to add line numbers to a given C program file
 */
#include <stdio.h>
int line_num = 1;
%}

%%
\n      { printf("%d\t", ++line_num); }
%%

int yywrap() { return 1; }

int main(int argc, char *argv[]) {
    printf("1\t");  // Print first line number
    yylex();
    return 0;
}
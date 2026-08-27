%{
#include <stdio.h>
%}

%%
[0-9]+      { printf("Number: %s\n", yytext); }
[a-zA-Z]+   { printf("Word: %s\n", yytext); }
[ \t\n]+    ;
.           { printf("Symbol: %s\n", yytext); }
%%

int yywrap()
{
    return 1;
}

int main()
{
    yylex();
    return 0;
}
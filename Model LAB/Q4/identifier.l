%{
#include <stdio.h>
%}

%%
^[a-zA-Z_][a-zA-Z0-9_]*$    { printf("Valid identifier: %s", yytext); }
.*                           { printf("Invalid identifier: %s", yytext); }
%%

int yywrap()
{
    return 1;
}

int main()
{
    yyin = fopen("sample.txt", "r");

    if (!yyin)
    {
        printf("Cannot open sample.txt\n");
        return 1;
    }

    yylex();

    fclose(yyin);
    return 0;
}
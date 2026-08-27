%{
#include <stdio.h>
%}

%%
[0-9]+      printf("Integer constant: %s\n", yytext);
[ \t\n]+    ;
.           ;
%%

int yywrap()
{
    return 1;
}

int main()
{
    yyin = fopen("sample.c", "r");

    if (yyin == NULL)
    {
        printf("Cannot open sample.c\n");
        return 1;
    }

    yylex();

    fclose(yyin);

    return 0;
}
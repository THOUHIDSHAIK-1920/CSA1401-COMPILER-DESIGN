%{
/*
 * Experiment 24: LEX program to count comment lines and eliminate them, writing to another file
 */
#include <stdio.h>
int comment_lines = 0;
%}

%x COMMENT
%%

"//" { comment_lines++; }

"/*" { comment_lines++; BEGIN COMMENT; }

<COMMENT>"*/" { BEGIN INITIAL; }
<COMMENT>.|\n { }

"//"[^\n]*   { comment_lines++; ECHO; }
"/*"         { comment_lines++; BEGIN COMMENT; }
\n           { ECHO; }
.            { ECHO; }
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
    yyout = fopen("output_without_comments.c", "w");
    if (!yyout) {
        printf("Error creating output file\n");
        return 1;
    }
    yylex();
    printf("Number of comment lines: %d\n", comment_lines);
    printf("Output written to output_without_comments.c\n");
    fclose(yyin);
    fclose(yyout);
    return 0;
}
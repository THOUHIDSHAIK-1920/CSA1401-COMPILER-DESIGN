/* 
 * Experiment 13: Top-Down / Bottom-Up Parsing to check if input string satisfies grammar
 * Grammar used: E -> i (simple expression grammar)
 * Using Top-Down (Recursive Descent) parsing
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

char input[100];
int pos = 0;
int error = 0;

// Grammar: E -> i | E + E | E * E | (E)
// We implement a simple recursive descent for a non-left-recursive version:
// E -> i | (E) | E + E | E * E
// Simplified: just check balanced parentheses, operators, and identifiers

void E() {
    if (input[pos] == '(') {
        pos++;
        E();
        if (input[pos] == ')')
            pos++;
        else
            error = 1;
    } else if (isalpha(input[pos])) {
        while (isalnum(input[pos])) pos++;
    } else {
        error = 1;
    }
    
    // Handle operators
    while (input[pos] == '+' || input[pos] == '*') {
        pos++;
        if (input[pos] == '(') {
            pos++;
            E();
            if (input[pos] == ')')
                pos++;
            else
                error = 1;
        } else if (isalpha(input[pos])) {
            while (isalnum(input[pos])) pos++;
        } else {
            error = 1;
        }
    }
}

int main() {
    printf("Top-Down Parser (Recursive Descent)\n");
    printf("Grammar: E -> i | E+E | E*E | (E)\n\n");
    
    printf("Enter input string: ");
    scanf("%s", input);
    pos = 0;
    error = 0;
    
    E();
    
    if (!error && input[pos] == '\0')
        printf("Result: String SATISFIES the grammar (ACCEPTED).\n");
    else
        printf("Result: String DOES NOT SATISFY the grammar (REJECTED).\n");
    
    return 0;
}
/* 
 * Experiment 4: Lexical Analyzer to validate operators +, -, *, / using regular arithmetic operators
 */
#include <stdio.h>
#include <ctype.h>

int main() {
    char input[100];
    int i;

    printf("Enter an expression with operators (+, -, *, /): ");
    fgets(input, sizeof(input), stdin);

    printf("\nOperators found:\n");
    printf("----------------\n");

    for (i = 0; input[i] != '\0'; i++) {
        switch (input[i]) {
            case '+':
                printf("Addition Operator: +\n");
                break;
            case '-':
                printf("Subtraction Operator: -\n");
                break;
            case '*':
                printf("Multiplication Operator: *\n");
                break;
            case '/':
                printf("Division Operator: /\n");
                break;
            default:
                break;
        }
    }

    return 0;
}
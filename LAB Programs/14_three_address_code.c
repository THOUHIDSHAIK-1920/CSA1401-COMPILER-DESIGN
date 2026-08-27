/* 
 * Experiment 14: Generate Three Address Code for a given input expression
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

char expr[MAX];
char temp[10];
int t_count = 1;

void generate_TAC(char op, char *arg1, char *arg2, char *result) {
    printf("%s = %s %c %s\n", result, arg1, op, arg2);
}

int is_operator(char ch) {
    return (ch == '+' || ch == '-' || ch == '*' || ch == '/');
}

int precedence(char op) {
    if (op == '*' || op == '/') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}

int main() {
    char stack[MAX][10];
    char ops[MAX];
    int top = -1, optop = -1;
    int i;
    char arg1[10], arg2[10], result[10];
    
    printf("Enter an arithmetic expression: ");
    scanf("%s", expr);
    
    printf("\nThree Address Code:\n");
    printf("--------------------\n");
    
    for (i = 0; expr[i] != '\0'; i++) {
        if (isalnum(expr[i])) {
            char operand[2] = {expr[i], '\0'};
            top++;
            strcpy(stack[top], operand);
        } else if (expr[i] == '(') {
            optop++;
            ops[optop] = expr[i];
        } else if (expr[i] == ')') {
            while (optop >= 0 && ops[optop] != '(') {
                char op = ops[optop];
                optop--;
                strcpy(arg2, stack[top]); top--;
                strcpy(arg1, stack[top]); top--;
                sprintf(result, "t%d", t_count++);
                generate_TAC(op, arg1, arg2, result);
                top++;
                strcpy(stack[top], result);
            }
            optop--; // Remove '('
        } else if (is_operator(expr[i])) {
            while (optop >= 0 && precedence(ops[optop]) >= precedence(expr[i])) {
                char op = ops[optop];
                optop--;
                strcpy(arg2, stack[top]); top--;
                strcpy(arg1, stack[top]); top--;
                sprintf(result, "t%d", t_count++);
                generate_TAC(op, arg1, arg2, result);
                top++;
                strcpy(stack[top], result);
            }
            optop++;
            ops[optop] = expr[i];
        }
    }
    
    while (optop >= 0) {
        char op = ops[optop];
        optop--;
        strcpy(arg2, stack[top]); top--;
        strcpy(arg1, stack[top]); top--;
        sprintf(result, "t%d", t_count++);
        generate_TAC(op, arg1, arg2, result);
        top++;
        strcpy(stack[top], result);
    }
    
    printf("\nFinal result stored in: %s\n", stack[top]);
    
    return 0;
}
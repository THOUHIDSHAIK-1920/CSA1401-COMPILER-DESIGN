/* 
 * Experiment 16: Back end of the compiler - Code Generation
 * Generates assembly-like code from three address code
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

int main() {
    int num;
    printf("=== BACK END OF COMPILER ===\n");
    printf("(Simulates code generation from intermediate code)\n\n");
    
    printf("Enter number of three-address code statements: ");
    scanf("%d", &num);
    
    char tac[MAX][MAX];
    printf("Enter the TAC statements (e.g., t1 = a + b):\n");
    for (int i = 0; i < num; i++) {
        scanf(" %[^\n]", tac[i]);
    }
    
    printf("\nGenerated Assembly Code:\n");
    printf("------------------------\n");
    
    for (int i = 0; i < num; i++) {
        char result[20], arg1[20], op[5], arg2[20];
        if (sscanf(tac[i], "%s = %s %s %s", result, arg1, op, arg2) == 4) {
            printf("MOV R0, %s\n", arg1);
            if (strcmp(op, "+") == 0) printf("ADD R0, %s\n", arg2);
            else if (strcmp(op, "-") == 0) printf("SUB R0, %s\n", arg2);
            else if (strcmp(op, "*") == 0) printf("MUL R0, %s\n", arg2);
            else if (strcmp(op, "/") == 0) printf("DIV R0, %s\n", arg2);
            printf("MOV %s, R0\n", result);
            printf("\n");
        }
    }
    
    return 0;
}
#include <stdio.h>
#include <string.h>

int main()
{
    char op[10], arg1[10], arg2[10], result[10];

    printf("Enter the three address code:\n");
    printf("Example: t1 = a + b\n\n");

    printf("Enter result: ");
    scanf("%s", result);

    printf("Enter operator: ");
    scanf("%s", op);

    printf("Enter operand 1: ");
    scanf("%s", arg1);

    printf("Enter operand 2: ");
    scanf("%s", arg2);

    printf("\nGenerated Target Code:\n");

    if (strcmp(op, "+") == 0)
        printf("MOV R0, %s\nADD R0, %s\nMOV %s, R0\n",
               arg1, arg2, result);

    else if (strcmp(op, "-") == 0)
        printf("MOV R0, %s\nSUB R0, %s\nMOV %s, R0\n",
               arg1, arg2, result);

    else if (strcmp(op, "*") == 0)
        printf("MOV R0, %s\nMUL R0, %s\nMOV %s, R0\n",
               arg1, arg2, result);

    else if (strcmp(op, "/") == 0)
        printf("MOV R0, %s\nDIV R0, %s\nMOV %s, R0\n",
               arg1, arg2, result);

    else
        printf("Invalid operator\n");

    return 0;
}
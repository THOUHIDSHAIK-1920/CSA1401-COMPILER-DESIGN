#include <stdio.h>
#include <string.h>

int main()
{
    int n, i, j;
    char code[20][50];
    char result[20][20], arg1[20][20], arg2[20][20], op[20][5];

    printf("Enter number of statements: ");
    scanf("%d", &n);

    getchar();

    printf("\nEnter Three Address Code:\n");

    for (i = 0; i < n; i++)
    {
        fgets(code[i], sizeof(code[i]), stdin);
        code[i][strcspn(code[i], "\n")] = '\0';

        sscanf(code[i], "%s = %s %s %s",
               result[i], arg1[i], op[i], arg2[i]);
    }

    printf("\nOriginal Code:\n");

    for (i = 0; i < n; i++)
    {
        printf("%s\n", code[i]);
    }

    printf("\nOptimized Code:\n");

    for (i = 0; i < n; i++)
    {
        int found = 0;

        for (j = 0; j < i; j++)
        {
            if (strcmp(arg1[i], arg1[j]) == 0 &&
                strcmp(op[i], op[j]) == 0 &&
                strcmp(arg2[i], arg2[j]) == 0)
            {
                printf("%s = %s\n", result[i], result[j]);
                found = 1;
                break;
            }
        }

        if (!found)
        {
            if (strlen(op[i]) > 0)
                printf("%s = %s %s %s\n",
                       result[i], arg1[i], op[i], arg2[i]);
            else
                printf("%s\n", code[i]);
        }
    }

    return 0;
}
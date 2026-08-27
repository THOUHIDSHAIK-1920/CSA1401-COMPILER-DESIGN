/* 
 * Experiment 7: Find FIRST() - Predictive Parser
 * Grammar: S -> AaAb | BbBa
 *          A -> epsilon
 *          B -> epsilon
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 10

char productions[MAX][MAX];
int num_productions = 0;

void add_production(char *prod) {
    strcpy(productions[num_productions++], prod);
}

void find_first(char symbol) {
    if (!isupper(symbol)) {
        printf(" %c ", symbol);
        return;
    }
    for (int i = 0; i < num_productions; i++) {
        char lhs = productions[i][0];
        if (lhs == symbol) {
            // Find the RHS after "->"
            char *rhs = strstr(productions[i], "->");
            if (rhs) {
                rhs += 2;
                while (*rhs == ' ') rhs++;
                if (*rhs == 'e' || *rhs == 'E') {
                    // epsilon production - check next symbol or add epsilon
                    printf(" e ");
                } else {
                    find_first(*rhs);
                }
            }
        }
    }
}

int main() {
    printf("Grammar:\n");
    printf("S -> AaAb | BbBa\n");
    printf("A -> epsilon\n");
    printf("B -> epsilon\n\n");

    add_production("S->AaAb");
    add_production("S->BbBa");
    add_production("A->e");
    add_production("B->e");

    printf("FIRST sets:\n");
    printf("-----------\n");
    
    printf("FIRST(S) = {");
    find_first('S');
    printf("}\n");
    
    printf("FIRST(A) = {");
    find_first('A');
    printf("}\n");
    
    printf("FIRST(B) = {");
    find_first('B');
    printf("}\n");

    return 0;
}
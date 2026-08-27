/* 
 * Experiment 8: Find FOLLOW() - Predictive Parser
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

int is_nonterminal(char c) {
    return isupper(c);
}

void find_first_from_rhs(char *rhs, int pos) {
    if (rhs[pos] == '\0') return;
    if (!is_nonterminal(rhs[pos])) {
        printf(" %c ", rhs[pos]);
        return;
    }
    // For this simple grammar, non-terminals A and B derive epsilon
    // So we just return the next terminal
    if (rhs[pos] == 'A' || rhs[pos] == 'B') {
        if (rhs[pos+1] != '\0') {
            if (!is_nonterminal(rhs[pos+1]))
                printf(" %c ", rhs[pos+1]);
        }
    }
}

void find_follow(char symbol) {
    if (symbol == 'S') {
        printf(" $ ");
    }
    for (int i = 0; i < num_productions; i++) {
        char *rhs = strstr(productions[i], "->");
        if (rhs) {
            rhs += 2;
            while (*rhs == ' ') rhs++;
            for (int j = 0; rhs[j] != '\0'; j++) {
                if (rhs[j] == symbol) {
                    // Check if there's a next symbol
                    if (rhs[j+1] != '\0') {
                        if (!is_nonterminal(rhs[j+1])) {
                            printf(" %c ", rhs[j+1]);
                        } else {
                            // Non-terminal after - find first of it
                            // For A and B which derive epsilon, just continue
                            if (rhs[j+1] == 'A' || rhs[j+1] == 'B') {
                                if (rhs[j+2] != '\0' && !is_nonterminal(rhs[j+2]))
                                    printf(" %c ", rhs[j+2]);
                            }
                        }
                    } else {
                        // symbol is at end of RHS, add FOLLOW of LHS
                        if (productions[i][0] != symbol)
                            find_follow(productions[i][0]);
                    }
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

    printf("FOLLOW sets:\n");
    printf("------------\n");
    
    printf("FOLLOW(S) = {");
    find_follow('S');
    printf("}\n");
    
    printf("FOLLOW(A) = {");
    find_follow('A');
    printf("}\n");
    
    printf("FOLLOW(B) = {");
    find_follow('B');
    printf("}\n");

    return 0;
}
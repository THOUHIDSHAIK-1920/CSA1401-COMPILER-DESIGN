/* 
 * Experiment 18: Compute TRAILING() - Operator Precedence Parser
 * Grammar: E -> E + T | T
 *          T -> T * F | F
 *          F -> (E) | id
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 10

typedef struct {
    char nonterm;
    char trailing[MAX];
    int count;
} TrailingSet;

TrailingSet trailing_sets[10];
int num_sets = 0;

void add_trailing(char nonterm, char symbol) {
    for (int i = 0; i < num_sets; i++) {
        if (trailing_sets[i].nonterm == nonterm) {
            for (int j = 0; j < trailing_sets[i].count; j++) {
                if (trailing_sets[i].trailing[j] == symbol)
                    return;
            }
            trailing_sets[i].trailing[trailing_sets[i].count++] = symbol;
            return;
        }
    }
    trailing_sets[num_sets].nonterm = nonterm;
    trailing_sets[num_sets].trailing[0] = symbol;
    trailing_sets[num_sets].count = 1;
    num_sets++;
}

int main() {
    printf("Grammar:\n");
    printf("E -> E + T | T\n");
    printf("T -> T * F | F\n");
    printf("F -> (E) | id\n\n");

    // Compute TRAILING
    // TRAILING(F) = { ), id }
    // TRAILING(T) = { *, ), id }
    // TRAILING(E) = { +, *, ), id }
    
    add_trailing('F', ')');
    add_trailing('F', 'i');  // id
    
    add_trailing('T', '*');
    add_trailing('T', ')');
    add_trailing('T', 'i');
    
    add_trailing('E', '+');
    add_trailing('E', '*');
    add_trailing('E', ')');
    add_trailing('E', 'i');
    
    printf("TRAILING sets:\n");
    printf("--------------\n");
    
    for (int i = 0; i < num_sets; i++) {
        printf("TRAILING(%c) = { ", trailing_sets[i].nonterm);
        for (int j = 0; j < trailing_sets[i].count; j++) {
            if (trailing_sets[i].trailing[j] == 'i')
                printf("id");
            else
                printf("%c", trailing_sets[i].trailing[j]);
            if (j < trailing_sets[i].count - 1)
                printf(", ");
        }
        printf(" }\n");
    }
    
    return 0;
}
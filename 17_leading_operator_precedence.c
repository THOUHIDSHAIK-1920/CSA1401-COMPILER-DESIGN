/* 
 * Experiment 17: Compute LEADING() - Operator Precedence Parser
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
    char leading[MAX];
    int count;
} LeadingSet;

LeadingSet leading_sets[10];
int num_sets = 0;

void add_leading(char nonterm, char symbol) {
    for (int i = 0; i < num_sets; i++) {
        if (leading_sets[i].nonterm == nonterm) {
            for (int j = 0; j < leading_sets[i].count; j++) {
                if (leading_sets[i].leading[j] == symbol)
                    return;
            }
            leading_sets[i].leading[leading_sets[i].count++] = symbol;
            return;
        }
    }
    // Create new entry
    leading_sets[num_sets].nonterm = nonterm;
    leading_sets[num_sets].leading[0] = symbol;
    leading_sets[num_sets].count = 1;
    num_sets++;
}

int main() {
    printf("Grammar:\n");
    printf("E -> E + T | T\n");
    printf("T -> T * F | F\n");
    printf("F -> (E) | id\n\n");

    // Compute LEADING
    // LEADING(F) = { (, id }
    // LEADING(T) = { *, (, id }
    // LEADING(E) = { +, *, (, id }
    
    add_leading('F', '(');
    add_leading('F', 'i');  // id
    
    add_leading('T', '*');
    add_leading('T', '(');
    add_leading('T', 'i');
    
    add_leading('E', '+');
    add_leading('E', '*');
    add_leading('E', '(');
    add_leading('E', 'i');
    
    printf("LEADING sets:\n");
    printf("--------------\n");
    
    for (int i = 0; i < num_sets; i++) {
        printf("LEADING(%c) = { ", leading_sets[i].nonterm);
        for (int j = 0; j < leading_sets[i].count; j++) {
            if (leading_sets[i].leading[j] == 'i')
                printf("id");
            else
                printf("%c", leading_sets[i].leading[j]);
            if (j < leading_sets[i].count - 1)
                printf(", ");
        }
        printf(" }\n");
    }
    
    return 0;
}
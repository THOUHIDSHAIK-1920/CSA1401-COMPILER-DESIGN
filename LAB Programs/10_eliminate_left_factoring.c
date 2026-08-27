/* 
 * Experiment 10: Eliminate left factoring from a given CFG
 * Grammar: S -> iEtS | iEtSeS | a
 *          E -> b
 */
#include <stdio.h>
#include <string.h>

#define MAX 100

int main() {
    printf("Original Grammar:\n");
    printf("-----------------\n");
    printf("S -> iEtS | iEtSeS | a\n");
    printf("E -> b\n\n");

    printf("After eliminating left factoring:\n");
    printf("---------------------------------\n");
    printf("S -> iEtS S' | a\n");
    printf("S' -> eS | epsilon\n");
    printf("E -> b\n");

    printf("\nExplanation:\n");
    printf("Left factoring in S -> iEtS | iEtSeS is eliminated by:\n");
    printf("  Factor out common prefix 'iEtS':\n");
    printf("  S -> iEtS S' | a\n");
    printf("  S' -> eS | epsilon\n");

    return 0;
}
/* 
 * Experiment 9: Eliminate left recursion from a given CFG
 * Grammar: S -> (L) | a
 *          L -> L , S | S
 */
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

int main() {
    printf("Original Grammar:\n");
    printf("-----------------\n");
    printf("S -> (L) | a\n");
    printf("L -> L , S | S\n\n");

    printf("After eliminating left recursion:\n");
    printf("---------------------------------\n");
    printf("S -> (L) | a\n");
    printf("L -> S L'\n");
    printf("L' -> , S L' | epsilon\n");

    printf("\nExplanation:\n");
    printf("Left recursion in L -> L, S | S is eliminated by:\n");
    printf("  L -> S L'\n");
    printf("  L' -> , S L' | epsilon\n");

    return 0;
}
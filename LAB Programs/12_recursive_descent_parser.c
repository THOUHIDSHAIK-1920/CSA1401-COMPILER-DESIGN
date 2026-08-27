/* 
 * Experiment 12: Recursive Descent Parsing
 * Grammar: E -> TE'
 *          E' -> +TE' | epsilon
 *          T -> FT'
 *          T' -> *FT' | epsilon
 *          F -> (E) | id
 */
#include <stdio.h>
#include <ctype.h>
#include <string.h>

char input[100];
int pos = 0;
int error = 0;

void E();
void Eprime();
void T();
void Tprime();
void F();

void match(char expected) {
    if (input[pos] == expected) {
        pos++;
    } else {
        error = 1;
    }
}

void E() {
    T();
    Eprime();
}

void Eprime() {
    if (input[pos] == '+') {
        match('+');
        T();
        Eprime();
    }
    // else epsilon - do nothing
}

void T() {
    F();
    Tprime();
}

void Tprime() {
    if (input[pos] == '*') {
        match('*');
        F();
        Tprime();
    }
    // else epsilon - do nothing
}

void F() {
    if (input[pos] == '(') {
        match('(');
        E();
        if (input[pos] == ')')
            match(')');
        else
            error = 1;
    } else if (isalpha(input[pos])) {
        // id - one or more letters
        while (isalpha(input[pos])) pos++;
    } else {
        error = 1;
    }
}

int main() {
    printf("Grammar:\n");
    printf("E -> TE'\n");
    printf("E' -> +TE' | epsilon\n");
    printf("T -> FT'\n");
    printf("T' -> *FT' | epsilon\n");
    printf("F -> (E) | id\n\n");

    printf("Enter input string: ");
    scanf("%s", input);
    pos = 0;
    error = 0;

    E();

    if (!error && input[pos] == '\0')
        printf("Result: String is ACCEPTED by the grammar.\n");
    else
        printf("Result: String is REJECTED by the grammar.\n");

    return 0;
}
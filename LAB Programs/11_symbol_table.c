/* 
 * Experiment 11: Symbol table operations
 * Operations: Insert, Display, Search, Delete
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX 100
#define TABLE_SIZE 100

typedef struct {
    char name[50];
    char type[20];
    char value[50];
    int scope;
} Symbol;

Symbol table[TABLE_SIZE];
int count = 0;

void insert() {
    if (count >= TABLE_SIZE) {
        printf("Symbol table is full!\n");
        return;
    }
    printf("Enter symbol name: ");
    scanf("%s", table[count].name);
    printf("Enter type (int/float/char/etc): ");
    scanf("%s", table[count].type);
    printf("Enter value: ");
    scanf("%s", table[count].value);
    printf("Enter scope level: ");
    scanf("%d", &table[count].scope);
    printf("Symbol inserted successfully!\n\n");
    count++;
}

void display() {
    if (count == 0) {
        printf("Symbol table is empty!\n\n");
        return;
    }
    printf("\n%-15s %-15s %-15s %-10s\n", "Name", "Type", "Value", "Scope");
    printf("--------------------------------------------------------\n");
    for (int i = 0; i < count; i++) {
        printf("%-15s %-15s %-15s %-10d\n", table[i].name, table[i].type, table[i].value, table[i].scope);
    }
    printf("\n");
}

void search() {
    char name[50];
    printf("Enter symbol name to search: ");
    scanf("%s", name);
    for (int i = 0; i < count; i++) {
        if (strcmp(table[i].name, name) == 0) {
            printf("\nSymbol found!\n");
            printf("Name: %s\n", table[i].name);
            printf("Type: %s\n", table[i].type);
            printf("Value: %s\n", table[i].value);
            printf("Scope: %d\n\n", table[i].scope);
            return;
        }
    }
    printf("Symbol '%s' not found!\n\n", name);
}

void delete() {
    char name[50];
    int found = 0;
    printf("Enter symbol name to delete: ");
    scanf("%s", name);
    for (int i = 0; i < count; i++) {
        if (strcmp(table[i].name, name) == 0) {
            for (int j = i; j < count - 1; j++) {
                table[j] = table[j + 1];
            }
            count--;
            found = 1;
            printf("Symbol deleted successfully!\n\n");
            break;
        }
    }
    if (!found)
        printf("Symbol '%s' not found!\n\n", name);
}

int main() {
    int choice;
    printf("=== SYMBOL TABLE OPERATIONS ===\n\n");
    
    while (1) {
        printf("1. Insert\n");
        printf("2. Display\n");
        printf("3. Search\n");
        printf("4. Delete\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: insert(); break;
            case 2: display(); break;
            case 3: search(); break;
            case 4: delete(); break;
            case 5: printf("Exiting...\n"); return 0;
            default: printf("Invalid choice!\n\n");
        }
    }
    return 0;
}
/*
Problema 1067 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int x, i;

    scanf("%d", &x);

    for (i = 1; i <= x; i += 2) {
        printf("%d\n", i);
    }

    return 0;
}
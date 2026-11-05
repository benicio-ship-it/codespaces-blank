/*
Problema 1073 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int n, i;

    scanf("%d", &n);

    for (i = 2; i <= n; i += 2) {
        printf("%d^2 = %d\n", i, i * i);
    }

    return 0;
}
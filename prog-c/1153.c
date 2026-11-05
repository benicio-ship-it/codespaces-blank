/*
Problema 1153 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int n, i;
    long long fatorial = 1;

    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        fatorial *= i;
    }

    printf("%lld\n", fatorial);

    return 0;
}
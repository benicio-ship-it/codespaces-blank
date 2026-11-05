/*
Problema 1164 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int n, i;
    long long x;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%lld", &x);
        long long soma = 0;

        for (long long j = 1; j * j <= x; j++) {
            if (x % j == 0) {
                if (j == 1) {
                    soma += 1;
                } else {
                    soma += j;
                    if (j * j != x) {
                        soma += x / j;
                    }
                }
            }
        }

        if (soma == x && x > 1) {
            printf("%lld eh perfeito\n", x);
        } else {
            printf("%lld nao eh perfeito\n", x);
        }
    }

    return 0;
}
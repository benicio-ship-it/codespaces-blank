/*
Problema 1165 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int n, x, i, j, eh_primo;

    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        eh_primo = 1;

        for (j = 2; j * j <= x; j++) {
            if (x % j == 0) {
                eh_primo = 0;
                break;
            }
        }

        if (eh_primo && x > 1) {
            printf("%d eh primo\n", x);
        } else {
            printf("%d nao eh primo\n", x);
        }
    }

    return 0;
}
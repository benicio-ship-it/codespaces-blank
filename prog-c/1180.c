/*
Problema 1180 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int n;

    scanf("%d", &n);

    int x[n];
    int menor, posicao = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &x[i]);
        if (i == 0 || x[i] < menor) {
            menor = x[i];
            posicao = i;
        }
    }

    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);

    return 0;
}
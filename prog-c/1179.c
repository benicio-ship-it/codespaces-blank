/*
Problema 1179 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int par[5], impar[5];
    int p = 0, i = 0;
    int valor;

    for (int k = 0; k < 15; k++) {
        scanf("%d", &valor);

        if (valor % 2 == 0 || valor % 2 == -2) { // Considera números pares (incluindo negativos)
            par[p] = valor;
            p++;
            if (p == 5) {
                for (int j = 0; j < 5; j++) {
                    printf("par[%d] = %d\n", j, par[j]);
                }
                p = 0;
            }
        } else {
            impar[i] = valor;
            i++;
            if (i == 5) {
                for (int j = 0; j < 5; j++) {
                    printf("impar[%d] = %d\n", j, impar[j]);
                }
                i = 0;
            }
        }
    }

    // Imprime os elementos restantes do vetor ímpar
    for (int j = 0; j < i; j++) {
        printf("impar[%d] = %d\n", j, impar[j]);
    }

    // Imprime os elementos restantes do vetor par
    for (int j = 0; j < p; j++) {
        printf("par[%d] = %d\n", j, par[j]);
    }

    return 0;
}
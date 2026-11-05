/*
Problema 1114 BeeCrowd
13.10.26
Benício Cordeiro
*/

#include <stdio.h>

int main() {
    int senha;

    while (1) {
        scanf("%d", &senha);
        
        if (senha == 2002) {
            printf("Acesso Permitido\n");
            break;
        } else {
            printf("Senha Invalida\n");
        }
    }

    return 0;
}
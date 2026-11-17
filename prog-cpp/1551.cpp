/*
Problema 1551 BeeCrowd
2026.11.05
Benício Cordeiro
*/

#include <iostream>
#include <string>
using namespace std;

int conta_letras(string frase) {
    int total = 0, i, tam = frase.size();
    char letra;
    bool achou;

    for (letra = 'a'; letra <= 'z'; letra++) {
        achou = false;
        for (i = 0; i < tam; i++) {
            if (frase[i] == letra) {
                achou = true;
            }
        }
        if (achou) {
            total++;
        }
    }
    return total;
}

int main() {
    int n, i, letras;
    string frase;

    cin >> n;
    cin.ignore();
    for (i = 0; i < n; i++) {
        getline(cin, frase);
        letras = conta_letras(frase);
        if (letras == 26) {
            cout << "frase completa" << endl;
        } else if (letras >= 13) {
            cout << "frase quase completa" << endl;
        } else {
            cout << "frase mal elaborada" << endl;
        }
    }

    return 0;
}
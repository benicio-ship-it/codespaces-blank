/*
Problema 1068 BeeCrowd
2026.11.05
Benício Cordeiro
*/
#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;

    // Tabela com a quantidade de LEDs para os dígitos de 0 a 9
    int leds_por_digito[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    while (n--) {
        string valor;
        cin >> valor;

        int total_leds = 0;
        for (char c : valor) {
            total_leds += leds_por_digito[c - '0'];
        }

        cout << total_leds << " leds" << endl;
    }

    return 0;
}
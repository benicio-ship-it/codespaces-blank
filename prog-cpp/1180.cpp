/*
Problema 1180 BeeCrowd
2026.11.05
Benício Cordeiro
*/

#include <iostream>
#include <vector>

using namespace std;

int posicao_do_menor(vector<int> &v) {
    int i, pos = 0, qtd = v.size();

    for (i = 1; i < qtd; i++) {
        if (v[i] < v[pos]) {
            pos = i;
        }
    }
    return pos;
}

int main() {
    vector<int> v;
    int n, x, i, pos;

    cin >> n;
    for (i = 0; i < n; i++) {
        cin >> x;
        v.push_back(x);
    }

    pos = posicao_do_menor(v);

    cout << "Menor valor: " << v[pos] << endl;
    cout << "Posicao: " << pos << endl;

    return 0;
}